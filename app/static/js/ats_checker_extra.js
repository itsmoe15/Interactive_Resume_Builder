document.addEventListener('DOMContentLoaded', function() {
    const dropZone = document.getElementById('upload-section');
    const fileInput = document.getElementById('file-input');
    const uploadSection = document.getElementById('upload-section');
    const loadingSection = document.getElementById('loading-section');
    const resultsSection = document.getElementById('results-section');
    const tailoringSection = document.getElementById('tailoring-section');
    const cvIframe = document.getElementById('cv-iframe');
    const noCvMessage = document.getElementById('no-cv-message');

    // Drag and drop handlers
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });
    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if (files.length) {
            handleFile(files[0]);
        }
    });
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) {
            handleFile(e.target.files[0]);
        }
    });

    function handleFile(file) {
        // Check file type
        const allowedTypes = ['.pdf', '.doc', '.docx'];
        const fileExt = '.' + file.name.split('.').pop().toLowerCase();
        if (!allowedTypes.includes(fileExt)) {
            alert('Please upload a PDF or Word document');
            return;
        }
        // Show loading state
        uploadSection.classList.add('d-none');
        loadingSection.classList.remove('d-none');
        resultsSection.classList.add('d-none');
        // Create FormData and send file
        const formData = new FormData();
        formData.append('cv', file);
        fetch('/check-ats', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            displayResults(data);
        })
        .catch(error => {
            alert(error.message || 'An error occurred while analyzing your CV');
            uploadSection.classList.remove('d-none');
            loadingSection.classList.add('d-none');
        })
        .finally(() => {
            loadingSection.classList.add('d-none');
        });
    }

    function displayResults(data) {
        // Score ring
        document.getElementById('overall-score').textContent = data.overall_score ?? 0;
        // Rating badge
        const rating = document.getElementById('rating');
        rating.textContent = data.rating || 'N/A';
        rating.style.background = getRatingBg(data.rating);
        rating.style.color = getRatingText(data.rating);
        // Sub-scores
        const subScoresContainer = document.getElementById('sub-scores-container');
        subScoresContainer.innerHTML = '';
        if (data.sub_scores) {
            const categories = {
                file_format: 'File Format',
                layout_formatting: 'Layout & Formatting',
                sections_order: 'Sections Order',
                contact_information: 'Contact Information',
                professional_summary: 'Professional Summary',
                experience_education: 'Experience & Education',
                keywords_skills: 'Keywords & Skills',
                length: 'Length',
                language_grammar: 'Language & Grammar',
                ats_pitfalls: 'ATS Pitfalls',
                tailoring: 'Tailoring'
            };
            Object.entries(data.sub_scores).forEach(([key, value]) => {
                if (categories[key]) {
                    const percent = Math.round(value * 100);
                    subScoresContainer.innerHTML += `
                        <div class="ats-subscore-row">
                            <div class="ats-subscore-label">${categories[key]}</div>
                            <div class="ats-progress">
                                <div class="ats-progress-bar" style="width: ${percent}%;">${percent}%</div>
                            </div>
                        </div>
                    `;
                }
            });
        }
        // Issues
        const issuesContainer = document.getElementById('issues-container');
        issuesContainer.innerHTML = '';
        if (data.issues && data.issues.length) {
            data.issues.forEach((issue) => {
                issuesContainer.innerHTML += `
                    <div class="ats-issue-card">
                        <div class="ats-issue-title"><i class="fas fa-exclamation-circle"></i> ${issue.category}</div>
                        <div class="ats-issue-findings"><strong>Findings:</strong>
                            <ul>${issue.findings.map(f => `<li>${f}</li>`).join('')}</ul>
                        </div>
                        <div class="ats-issue-suggestions"><strong>Suggestions:</strong>
                            <ul>${issue.suggestions.map(s => `<li>${s}</li>`).join('')}</ul>
                        </div>
                    </div>
                `;
            });
        } else {
            issuesContainer.innerHTML = '<div class="alert alert-success" style="background: var(--primary); color: var(--bg-darkest); font-weight:700;">No major issues detected!</div>';
        }
        // Tailoring
        if (data.tailoring) {
            tailoringSection.classList.remove('d-none');
            const missingKeywordsList = document.getElementById('missing-keywords-list');
            const actionsList = document.getElementById('actions-list');
            missingKeywordsList.innerHTML = '';
            actionsList.innerHTML = '';
            if (data.tailoring.missing_keywords && data.tailoring.missing_keywords.length) {
                data.tailoring.missing_keywords.forEach(kw => {
                    missingKeywordsList.innerHTML += `<li>${kw}</li>`;
                });
            } else {
                missingKeywordsList.innerHTML = '<li>None</li>';
            }
            if (data.tailoring.actions && data.tailoring.actions.length) {
                data.tailoring.actions.forEach(act => {
                    actionsList.innerHTML += `<li>${act}</li>`;
                });
            } else {
                actionsList.innerHTML = '<li>None</li>';
            }
        } else {
            tailoringSection.classList.add('d-none');
        }
        // Show results
        resultsSection.classList.remove('d-none');
        // Show CV preview if file_url is present
        if (data.file_url) {
            cvIframe.src = data.file_url;
            cvIframe.classList.remove('d-none');
            if (noCvMessage) noCvMessage.classList.add('d-none');
        }
    }

    function getRatingBg(rating) {
        switch(rating) {
            case 'Excellent': return 'var(--primary)';
            case 'Good': return 'linear-gradient(90deg, var(--primary), var(--primary-light))';
            case 'Moderate': return '#FFD600';
            case 'Poor': return '#FF3B3B';
            default: return 'var(--primary)';
        }
    }
    function getRatingText(rating) {
        switch(rating) {
            case 'Excellent':
            case 'Good': return 'var(--bg-darkest)';
            case 'Moderate': return 'var(--bg-darkest)';
            case 'Poor': return 'var(--text-primary)';
            default: return 'var(--bg-darkest)';
        }
    }
}); 