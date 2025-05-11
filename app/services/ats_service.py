import base64
import json
from google import genai
from google.genai import types

def analyze_cv(cv_content_base64):
    """
    Analyze a CV using Gemini AI and return ATS compatibility results.
    
    Args:
        cv_content_base64 (str): Base64 encoded CV content
        
    Returns:
        dict: Analysis results following the defined schema
    """
    client = genai.Client(
        api_key="AIzaSyAw8B_ipc_bXGndu_FVdrAtd5GiXocKb3g",
    )

    model = "gemini-2.5-flash-preview-04-17"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""Please analyze this CV for ATS compatibility. Here's the base64 encoded content:
                {cv_content_base64}
                
                Please provide a detailed analysis following the schema defined in the system instructions."""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            required = ["overall_score", "rating", "sub_scores", "issues"],
            properties = {
                "overall_score": genai.types.Schema(
                    type = genai.types.Type.INTEGER,
                    description = "Aggregated ATS compatibility score (0–100).",
                ),
                "rating": genai.types.Schema(
                    type = genai.types.Type.STRING,
                    description = "Qualitative label based on overall_score.",
                    enum = ["Excellent", "Good", "Moderate", "Poor"],
                ),
                "sub_scores": genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    description = "Individual check scores (0.0–1.0) weighted in final score calculation.",
                    required = ["file_format", "layout_formatting", "sections_order", "contact_information", "professional_summary", "experience_education", "keywords_skills", "length", "language_grammar", "ats_pitfalls"],
                    properties = {
                        "file_format": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "layout_formatting": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "sections_order": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "contact_information": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "professional_summary": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "experience_education": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "keywords_skills": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "length": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "language_grammar": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "ats_pitfalls": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                        ),
                        "tailoring": genai.types.Schema(
                            type = genai.types.Type.NUMBER,
                            description = "Only present and scored if a job description was provided.",
                        ),
                    },
                ),
                "issues": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    description = "List of categories with findings and suggestions.",
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["category", "findings", "suggestions"],
                        properties = {
                            "category": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Name of the check area (e.g., 'Experience & Education').",
                            ),
                            "findings": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                description = "Detected issues in this category.",
                                items = genai.types.Schema(
                                    type = genai.types.Type.STRING,
                                ),
                            ),
                            "suggestions": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                description = "Actionable recommendations for each finding.",
                                items = genai.types.Schema(
                                    type = genai.types.Type.STRING,
                                ),
                            ),
                        },
                    ),
                ),
                "tailoring": genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    description = "Only included if a job description was supplied.",
                    required = ["missing_keywords", "actions"],
                    properties = {
                        "missing_keywords": genai.types.Schema(
                            type = genai.types.Type.ARRAY,
                            description = "JD keywords not present in the CV.",
                            items = genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        ),
                        "actions": genai.types.Schema(
                            type = genai.types.Type.ARRAY,
                            description = "How to integrate those keywords into the CV.",
                            items = genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        ),
                    },
                ),
            },
        ),
        system_instruction=[
            types.Part.from_text(text="""

## System Instructions: ATS Compatibility Checker

**Your Role:**
You are an AI that ingests a user's CV (and optional job description), runs a battery of ATS‐focused checks, computes a weighted compatibility score (0–100), and returns a structured report with actionable feedback.

---

### 1. Inputs

* **Required:** CV document (Word/PDF).
* **Optional:** Job description text.

### 2. Processing Pipeline

1. **Parse**

   * Attempt to extract raw text and structural elements (headings, lists, tables).
   * If parsing fails, stop and ask user to re‐upload in `.docx` or text‐based PDF.

2. **Run Checks**
   Perform the following 11 checks in sequence. Each check returns:

   * **Pass/Fail** or **Degree of Compliance** (e.g. 0–1).
   * **Issues list** (textual findings).
   * **Suggestions list** (concrete next steps).

   | Check                             | Weight (%) |
   | --------------------------------- | ---------: |
   | 1. File Format                    |         5% |
   | 2. Layout & Formatting            |        10% |
   | 3. Section Titles & Order         |        10% |
   | 4. Contact Information            |         5% |
   | 5. Professional Summary/Objective |         5% |
   | 6. Experience & Education         |        20% |
   | 7. Keywords & Skills              |        15% |
   | 8. Length                         |         5% |
   | 9. Language & Grammar             |        10% |
   | 10. ATS‐Specific Pitfalls         |         5% |
   | 11. Tailoring to JD (if given)    |        10% |

3. **Score Calculation**

   * For each check *i*, compute a sub‐score Si between 0 and 1.
   * Overall score = ⎣100 × Σ(Wi × Si)⎦.
   * Map to label:

     * 90–100 → **Excellent**
     * 70–89  → **Good**
     * 50–69  → **Moderate**
     * < 50   → **Poor**

4. **Report Generation**
   Output a JSON‐style object (or equivalent structured text) with:

   1. **Overall Statement** ("Your CV scores 76/100 (Good).")
   2. **Score Breakdown** (sub‐scores for each check).
   3. **Consolidated Issues & Suggestions**, grouped by category and sorted by severity.
   4. **If JD Provided:** a "Tailoring" section listing missing JD keywords and how to integrate them.

5. **Privacy & Formatting**

   * Never retain or log CV text beyond the current session.
   * Return plain text or JSON—do not embed proprietary file content.

---

### 3. Check Details & Sample Scoring Logic

#### 1. File Format (5 %)

* **.doc/.docx** → S₁ = 1.0
* **Text‐based PDF** → S₁ = 0.7
* **Else** → S₁ = 0.0

#### 2. Layout & Formatting (10 %)

* Single column, standard fonts (Arial, Calibri, Times New Roman), 10–12 pt, minimal tables/images
* Score proportional to number of violations (e.g. if 2 of 5 criteria fail → S₂ = 0.6)

> *…and so on for checks 3–11, each with clear pass/fail rules or graded measures…*
-
```"""),
        ],
    )

    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=generate_content_config,
        )
        
        # Parse the response text as JSON
        result = json.loads(response.text)
        
        # Ensure all required fields are present
        required_fields = ["overall_score", "rating", "sub_scores", "issues"]
        for field in required_fields:
            if field not in result:
                raise ValueError(f"Missing required field: {field}")
        
        return result
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        print(f"Raw response: {response.text}")
        raise ValueError("Invalid response format from AI model")
    except Exception as e:
        print(f"Error in analyze_cv: {e}")
        raise 