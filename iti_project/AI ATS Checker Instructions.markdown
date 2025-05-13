# Instructions for Building an AI ATS Checker

This document provides comprehensive instructions for programming an AI to check CVs for Applicant Tracking System (ATS) compatibility. The AI will evaluate CVs and provide users with a report indicating whether their CV is ATS-compatible and, if not, offer specific suggestions for improvement. These instructions are based on industry-standard practices for ATS optimization.

## Overview
Applicant Tracking Systems (ATS) are software tools used by employers to manage job applications. They scan CVs for specific formatting, keywords, and content to filter candidates. A good ATS checker ensures a CV is readable by these systems and tailored to job requirements. The AI should perform a series of checks, assign a compatibility score, and provide actionable feedback.

## Detailed Checks
The AI should evaluate the CV against the following criteria:

### 1. File Format and Structure
- **Purpose:** Ensure the CV is in a format that ATS can parse.
- **Checks:**
  - Preferred file types: Word documents (.doc, .docx) are most reliable, as they are easily convertible by ATS ([TopResume](https://topresume.com/career-advice/ask-amanda-resume-ats-readability)).
  - PDFs are acceptable but may cause issues if not generated from text-based documents (e.g., scanned images are not readable).
  - Avoid: HTML, Open Office (.odt), Apple Pages (.pages), or plain text (.txt) unless specified by the employer.
- **Feedback Example:** "Your CV is in PDF format. Convert to a Word document (.docx) for better ATS compatibility."

### 2. Formatting and Layout
- **Purpose:** Confirm the CV uses an ATS-friendly layout.
- **Checks:**
  - Use a single-column layout to avoid parsing errors ([ResumeWorded](https://resumeworded.com/resume-scanner)).
  - Use standard fonts (e.g., Arial, Calibri, Times New Roman, Garamond) with a size of 10-12 points.
  - Ensure all text is left-aligned.
  - Avoid tables, images, charts, diagrams, headers, footers, or text boxes, as ATS cannot read these.
  - Use standard section titles (e.g., "Work Experience," "Education," "Skills").
- **Feedback Example:** "Your CV uses a two-column layout. Convert to a single-column layout to ensure ATS readability."

### 3. Section Titles and Order
- **Purpose:** Verify that sections are clearly labeled and logically ordered.
- **Checks:**
  - Typical order: Contact Information → Professional Summary → Work Experience → Education → Skills → Additional Sections (e.g., Certifications).
  - Use conventional titles (e.g., "Work Experience" instead of "Career Journey").
- **Feedback Example:** "The section titled 'My Career' should be renamed to 'Work Experience' for ATS compatibility."

### 4. Contact Information
- **Purpose:** Ensure contact details are clear and accessible.
- **Checks:**
  - Must include: Full name, phone number, email address.
  - Optional: LinkedIn profile or other professional links.
  - Place contact information at the top of the CV.
- **Feedback Example:** "Your CV lacks an email address. Add it to the Contact Information section."

### 5. Professional Summary
- **Purpose:** Confirm the presence of a concise summary highlighting qualifications.
- **Checks:**
  - Look for a 1-3 sentence summary at the start of the CV, outlining key skills and career goals.
- **Feedback Example:** "Add a Professional Summary to highlight your top skills and qualifications."

### 6. Work Experience and Education
- **Purpose:** Ensure these sections are ATS-friendly and well-structured.
- **Checks:**
  - List entries in reverse chronological order (most recent first).
  - Use consistent date formats (e.g., "January 2020 - March 2023").
  - For each entry:
    - Include job title, company name, and location.
    - Use bullet points starting with action verbs (e.g., "Led," "Developed").
    - Quantify achievements (e.g., "Increased sales by 20%") ([MyPerfectResume](https://www.myperfectresume.com/resume/ats-resume-checker)).
- **Feedback Example:** "Reformat dates in the Work Experience section to 'Month Year - Month Year' for consistency."

### 7. Keywords and Skills
- **Purpose:** Verify the inclusion of job-relevant keywords and skills.
- **Checks:**
  - Look for a "Skills" section listing hard and soft skills.
  - Check for general keywords (e.g., "project management," "data analysis") if no job description is provided.
  - If a job description is available, match keywords from it to the CV.
- **Feedback Example:** "Add keywords like 'data analysis' and 'Python' to the Skills section to align with your target role."

### 8. Length
- **Purpose:** Ensure the CV is concise yet comprehensive.
- **Checks:**
  - Ideal length: 1-2 pages (approximately 1,100-2,200 characters).
  - One page is often sufficient for early-career professionals.
- **Feedback Example:** "Your CV is three pages long. Condense it to 1-2 pages by focusing on relevant experience."

### 9. Language and Grammar
- **Purpose:** Confirm the CV is error-free and uses effective language.
- **Checks:**
  - Perform spelling and grammar checks.
  - Prefer active voice over passive voice.
  - Avoid overused phrases (e.g., "team player") and clichés.
- **Feedback Example:** "Replace 'Responsible for' with 'Managed' to use active voice in the Work Experience section."

### 10. ATS-Specific Checks
- **Purpose:** Identify elements that may confuse ATS.
- **Checks:**
  - Avoid unusual characters, symbols, or excessive formatting (e.g., heavy bolding).
  - Ensure all text is plain and parseable.
- **Feedback Example:** "Remove special characters in the Skills section to prevent ATS parsing errors."

### 11. Overall ATS Compatibility
- **Purpose:** Provide a summary of the CV’s ATS readiness.
- **Checks:**
  - Assign a score based on the above criteria:
    - 90-100%: Excellent
    - 70-89%: Good, minor improvements needed
    - 50-69%: Moderate, significant improvements needed
    - Below 50%: Poor, major revisions required
- **Feedback Example:** "Your CV scores 65/100. See below for specific improvements."

### 12. Tailoring to the Job (Optional)
- **Purpose:** Enhance relevance if a job description is provided.
- **Checks:**
  - Compare CV keywords, skills, and experiences to the job description.
- **Feedback Example:** "Emphasize 'project management' skills to better match the job description."

## Output Format
The AI should generate a report with:
- A statement on ATS compatibility.
- A score or grade (optional).
- Specific feedback with actionable suggestions.

### Example Output
```
**ATS Compatibility Check Result:**
Your CV is moderately ATS-compatible (Score: 65/100). Improvements are needed to pass ATS filters.

**Areas for Improvement:**
- **File Format:** Your CV is a PDF. Convert to a Word document (.docx).
- **Formatting:** The two-column layout may not parse correctly. Use a single-column layout.
- **Keywords:** Add keywords like 'data analysis' and 'Python' to the Skills section.
- **Work Experience:** Use consistent date formats (e.g., 'January 2020 - March 2023').
- **Grammar:** Correct spelling errors in the Education section.

**Suggestions:**
- Convert to a Word document.
- Switch to a single-column layout.
- Add relevant keywords.
- Standardize date formats.
- Proofread for spelling errors.
```

## Implementation Notes
- **User Input:** Allow users to upload a CV and optionally provide a job description.
- **Error Handling:** If the CV cannot be parsed, notify the user and suggest a compatible format.
- **Privacy:** Handle CV data securely, as it contains personal information.
- **Training:** Train the AI on ATS-friendly CVs to improve accuracy.

## Additional Considerations
- **Regional Differences:** These instructions focus on US-standard CVs, as ATS is widely used there. For global use, consider regional CV formats.
- **ATS Variability:** Different ATS platforms (e.g., Taleo, Workday) may have unique requirements, but these guidelines cover general best practices.
- **Statistics:** Only 15% of CVs typically pass ATS to reach recruiters, highlighting the importance of optimization ([MyPerfectResume](https://www.myperfectresume.com/resume/ats-resume-checker)).

## Summary Table
| **Check**                | **Details**                                                                 | **Feedback Example**                                                                 |
|--------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| File Format              | Prefer .doc, .docx; avoid scanned PDFs                                      | "Convert your PDF to a Word document."                                              |
| Formatting               | Single-column, standard fonts, no tables/images                             | "Switch to a single-column layout."                                                 |
| Section Titles           | Use standard titles (e.g., "Work Experience")                               | "Rename 'Career Journey' to 'Work Experience'."                                     |
| Contact Information      | Include name, phone, email at the top                                       | "Add your email address to the Contact Information section."                        |
| Professional Summary     | Concise summary of skills and goals                                         | "Add a Professional Summary highlighting your skills."                              |
| Work Experience          | Reverse chronological, action verbs, quantified achievements                | "Use 'Managed' instead of 'Responsible for' in bullet points."                      |
| Keywords                 | Include job-relevant skills and terms                                       | "Add 'data analysis' to the Skills section."                                        |
| Length                   | 1-2 pages                                                                  | "Condense your CV to 1-2 pages."                                                    |
| Language                 | Error-free, active voice, no clichés                                        | "Correct spelling errors in the Education section."                                 |
| ATS-Specific             | Avoid special characters, complex formatting                                | "Remove special characters from the Skills section."                                |

By implementing these instructions, your AI ATS checker will help users optimize their CVs for ATS compatibility, increasing their chances of reaching human recruiters.