// Resume data object
const resumeData = {
    personalInfo: {},
    education: [],
    experience: [],
    skills: [],
    template: 'modern'
};

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function () {
    // Add first education and experience entries by default
    addEducation();
    addExperience();

    // Update preview when any input changes
    document.querySelectorAll('input, textarea, select').forEach(element => {
        element.addEventListener('input', updatePreview);
    });

    // Work Experience Dynamic Addition
    const addWorkBtn = document.getElementById('add-work');
    const workContainer = document.getElementById('work-experience-container');
    
    if (addWorkBtn && workContainer) {
        addWorkBtn.addEventListener('click', function() {
            const workItems = workContainer.querySelectorAll('.work-experience-item');
            const newIndex = workItems.length;
            const newItem = createWorkExperienceItem(newIndex);
            workContainer.appendChild(newItem);
            
            // Add event listener to the new "Current Job" checkbox
            const newCheckbox = newItem.querySelector(`#currentJob${newIndex}`);
            if (newCheckbox) {
                newCheckbox.addEventListener('change', handleCurrentJobChange);
            }
            
            // Add event listener to the remove button
            const removeBtn = newItem.querySelector('.remove-item');
            if (removeBtn) {
                removeBtn.addEventListener('click', handleRemoveItem);
            }
        });
        
        // Add event listeners to existing "Current Job" checkboxes
        document.querySelectorAll('.current-job').forEach(checkbox => {
            checkbox.addEventListener('change', handleCurrentJobChange);
        });
    }
    
    // Education Dynamic Addition
    const addEducationBtn = document.getElementById('add-education');
    const educationContainer = document.getElementById('education-container');
    
    if (addEducationBtn && educationContainer) {
        addEducationBtn.addEventListener('click', function() {
            const educationItems = educationContainer.querySelectorAll('.education-item');
            const newIndex = educationItems.length;
            const newItem = createEducationItem(newIndex);
            educationContainer.appendChild(newItem);
            
            // Add event listener to the new "Current Education" checkbox
            const newCheckbox = newItem.querySelector(`#currentEducation${newIndex}`);
            if (newCheckbox) {
                newCheckbox.addEventListener('change', handleCurrentEducationChange);
            }
            
            // Add event listener to the remove button
            const removeBtn = newItem.querySelector('.remove-item');
            if (removeBtn) {
                removeBtn.addEventListener('click', handleRemoveItem);
            }
        });
        
        // Add event listeners to existing "Current Education" checkboxes
        document.querySelectorAll('.current-education').forEach(checkbox => {
            checkbox.addEventListener('change', handleCurrentEducationChange);
        });
    }
    
    // Add remove buttons to existing items and attach event listeners
    document.querySelectorAll('.work-experience-item, .education-item').forEach((item, index) => {
        if (index > 0) { // Don't add remove button to the first item
            const removeBtn = document.createElement('span');
            removeBtn.className = 'remove-item';
            removeBtn.innerHTML = '<i class="fas fa-times-circle"></i>';
            removeBtn.addEventListener('click', handleRemoveItem);
            item.appendChild(removeBtn);
        }
    });
    
    // Handle form submission
    const cvForm = document.getElementById('cv-form');
    if (cvForm) {
        cvForm.addEventListener('submit', function(e) {
            const requiredFields = cvForm.querySelectorAll('[required]');
            let allValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    allValid = false;
                    field.classList.add('is-invalid');
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!allValid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
                window.scrollTo(0, 0);
            }
        });
    }
});

// Navigation functions
function nextStep(currentStep) {
    document.querySelector(`.form-step[data-step="${currentStep}"]`).classList.remove('active');
    document.querySelector(`.form-step[data-step="${currentStep + 1}"]`).classList.add('active');
    updateProgressBar(currentStep + 1);
}

function prevStep(currentStep) {
    document.querySelector(`.form-step[data-step="${currentStep}"]`).classList.remove('active');
    document.querySelector(`.form-step[data-step="${currentStep - 1}"]`).classList.add('active');
    updateProgressBar(currentStep - 1);
}

function finishForm() {
    // You could add validation here before showing preview
    updatePreview();
}

function updateProgressBar(step) {
    const steps = document.querySelectorAll('.arrow-steps .step');
    steps.forEach((stepEl, idx) => {
        stepEl.classList.remove('current', 'done', 'active');
        if (idx + 1 < step) {
            stepEl.classList.add('done');
        } else if (idx + 1 === step) {
            stepEl.classList.add('current');
        }
    });
}

// Add new education entry
function addEducation() {
    const educationEntries = document.getElementById('education-entries');
    const educationId = Date.now();

    educationEntries.innerHTML += `
        <div class="education-entry" id="edu-${educationId}">
            <div class="form-group">
                <label for="degree-${educationId}">Degree/Certificate*</label>
                <input type="text" id="degree-${educationId}" required>
            </div>
            <div class="form-group">
                <label for="institution-${educationId}">Institution*</label>
                <input type="text" id="institution-${educationId}" required>
            </div>
            <div class="form-group">
                <label for="eduStartDate-${educationId}">Start Date*</label>
                <input type="date" id="eduStartDate-${educationId}" required>
            </div>
            <div class="form-group">
                <label for="eduEndDate-${educationId}">End Date (or Current)</label>
                <input type="date" id="eduEndDate-${educationId}">
            </div>
            <div class="form-group">
                <input type="checkbox" id="currentEducation-${educationId}" onchange="toggleCurrent('edu', '${educationId}')">
                <label for="currentEducation-${educationId}">Current Education</label>
            </div>
            <div class="form-group">
                <label for="eduDescription-${educationId}">Description</label>
                <textarea id="eduDescription-${educationId}"></textarea>
            </div>
            <button type="button" class="btn remove-btn" onclick="removeEducation('${educationId}')">Remove</button>
            <hr>
        </div>
    `;
}

// Remove education entry
function removeEducation(id) {
    document.getElementById(`edu-${id}`).remove();
    updatePreview();
}

// Add new work experience entry
function addExperience() {
    const experienceEntries = document.getElementById('experience-entries');
    const experienceId = Date.now();

    experienceEntries.innerHTML += `
        <div class="experience-entry" id="exp-${experienceId}">
            <div class="form-group">
                <label for="jobTitle-${experienceId}">Job Title*</label>
                <input type="text" id="jobTitle-${experienceId}" required>
            </div>
            <div class="form-group">
                <label for="company-${experienceId}">Company*</label>
                <input type="text" id="company-${experienceId}" required>
            </div>
            <div class="form-group">
                <label for="expStartDate-${experienceId}">Start Date*</label>
                <input type="date" id="expStartDate-${experienceId}" required>
            </div>
            <div class="form-group">
                <label for="expEndDate-${experienceId}">End Date (or Current)</label>
                <input type="date" id="expEndDate-${experienceId}">
            </div>
            <div class="form-group">
                <input type="checkbox" id="currentJob-${experienceId}" onchange="toggleCurrent('exp', '${experienceId}')">
                <label for="currentJob-${experienceId}">Current job</label>
            </div>
            <div class="form-group">
                <label for="description-${experienceId}">Description</label>
                <textarea id="description-${experienceId}"></textarea>
            </div>
            <button type="button" class="btn remove-btn" onclick="removeExperience('${experienceId}')">Remove</button>
            <hr>
        </div>
    `;
}

// Remove experience entry
function removeExperience(id) {
    document.getElementById(`exp-${id}`).remove();
    updatePreview();
}

// Toggle current job/education
function toggleCurrent(type, id) {
    const endDateField = type === 'edu'
        ? document.getElementById(`eduEndDate-${id}`)
        : document.getElementById(`expEndDate-${id}`);

    const currentCheckbox = type === 'edu'
        ? document.getElementById(`currentEducation-${id}`)
        : document.getElementById(`currentJob-${id}`);

    endDateField.disabled = currentCheckbox.checked;
    updatePreview();
}

// Change template style
function changeTemplate() {
    const template = document.getElementById('template-select').value;
    resumeData.template = template;

    // Remove all template classes
    document.body.classList.remove(
        'template-modern',
        'template-classic',
        'template-professional'
    );

    // Add selected template class
    document.body.classList.add(`template-${template}`);
}

// Update resume preview
function updatePreview() {
    // Update personal information
    document.getElementById('preview-name').textContent = document.getElementById('fullName').value || 'Your Name';
    document.getElementById('preview-title').textContent = document.getElementById('jobTitle').value || 'Job Title';

    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const address = document.getElementById('address').value;
    document.getElementById('preview-contact').textContent = [email, phone, address].filter(Boolean).join(' | ') || 'Contact Information';

    document.getElementById('preview-summary').textContent = document.getElementById('summary').value || 'Professional summary appears here...';

    // Update education
    const educationEntries = document.querySelectorAll('.education-entry');
    let educationHTML = '';

    educationEntries.forEach(entry => {
        const degree = entry.querySelector('input[type="text"]').value;
        const institution = entry.querySelectorAll('input[type="text"]')[1].value;
        const startDate = entry.querySelector('input[type="date"]').value;
        const endDate = entry.querySelectorAll('input[type="date"]')[1].value;
        const isCurrent = entry.querySelector('input[type="checkbox"]').checked;
        const description = entry.querySelector('textarea').value;

        if (degree || institution) {
            educationHTML += `
                <div class="preview-item">
                    <h4>${degree || 'Degree'} from ${institution || 'Institution'}</h4>
                    <p>${formatDate(startDate) || 'Start Date'} - ${isCurrent ? 'Present' : formatDate(endDate) || 'End Date'}</p>
                    ${description ? `<p>${description}</p>` : ''}
                </div>
            `;
        }
    });

    document.getElementById('preview-education').innerHTML = educationHTML || '<p>No education added</p>';

    // Update work experience
    const experienceEntries = document.querySelectorAll('.experience-entry');
    let experienceHTML = '';

    experienceEntries.forEach(entry => {
        const jobTitle = entry.querySelector('input[type="text"]').value;
        const company = entry.querySelectorAll('input[type="text"]')[1].value;
        const startDate = entry.querySelector('input[type="date"]').value;
        const endDate = entry.querySelectorAll('input[type="date"]')[1].value;
        const isCurrent = entry.querySelector('input[type="checkbox"]').checked;
        const description = entry.querySelector('textarea').value;

        if (jobTitle || company) {
            experienceHTML += `
                <div class="preview-item">
                    <h4>${jobTitle || 'Job Title'} at ${company || 'Company'}</h4>
                    <p>${formatDate(startDate) || 'Start Date'} - ${isCurrent ? 'Present' : formatDate(endDate) || 'End Date'}</p>
                    ${description ? `<p>${description}</p>` : ''}
                </div>
            `;
        }
    });

    document.getElementById('preview-experience').innerHTML = experienceHTML || '<p>No work experience added</p>';

    // Update skills
    const skills = document.getElementById('skills').value;
    if (skills) {
        const skillsList = skills.split(',')
            .map(skill => `<li>${skill.trim()}</li>`)
            .join('');
        document.getElementById('preview-skills').innerHTML = `<ul>${skillsList}</ul>`;
    } else {
        document.getElementById('preview-skills').innerHTML = '<p>No skills added</p>';
    }
}

// Format date for display
function formatDate(dateString) {
    if (!dateString) return '';

    const options = { year: 'numeric', month: 'short' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

// Export to PDF (placeholder - needs jsPDF library)
document.getElementById('export-pdf').addEventListener('click', function () {
    alert('PDF export will be implemented with jsPDF library');
    // Implementation would go here
});

// Helper Functions
function handleCurrentJobChange(e) {
    const endDateInput = e.target.closest('.col-md-6').querySelector('input[type="month"]');
    if (endDateInput) {
        endDateInput.disabled = e.target.checked;
        if (e.target.checked) {
            endDateInput.value = '';
        }
    }
}

function handleCurrentEducationChange(e) {
    const endDateInput = e.target.closest('.col-md-6').querySelector('input[type="month"]');
    if (endDateInput) {
        endDateInput.disabled = e.target.checked;
        if (e.target.checked) {
            endDateInput.value = '';
        }
    }
}

function handleRemoveItem(e) {
    const item = e.target.closest('.work-experience-item, .education-item');
    if (item) {
        if (confirm('Are you sure you want to remove this item?')) {
            item.remove();
        }
    }
}

function createWorkExperienceItem(index) {
    const div = document.createElement('div');
    div.className = 'work-experience-item mb-3 p-3 border rounded';
    div.innerHTML = `
        <div class="row g-3">
            <div class="col-md-6">
                <label class="form-label">Job Title*</label>
                <input type="text" class="form-control" name="workTitle[]" required>
            </div>
            <div class="col-md-6">
                <label class="form-label">Company*</label>
                <input type="text" class="form-control" name="workCompany[]" required>
            </div>
            <div class="col-md-6">
                <label class="form-label">Start Date*</label>
                <input type="month" class="form-control" name="workStartDate[]" required>
            </div>
            <div class="col-md-6">
                <label class="form-label">End Date (or Current)</label>
                <input type="month" class="form-control" name="workEndDate[]">
                <div class="form-check mt-2">
                    <input class="form-check-input current-job" type="checkbox" id="currentJob${index}" data-index="${index}">
                    <label class="form-check-label" for="currentJob${index}">Current Job</label>
                </div>
            </div>
            <div class="col-12">
                <label class="form-label">Description*</label>
                <textarea class="form-control" name="workDescription[]" rows="3" required></textarea>
            </div>
        </div>
        <span class="remove-item"><i class="fas fa-times-circle"></i></span>
    `;
    return div;
}

function createEducationItem(index) {
    const div = document.createElement('div');
    div.className = 'education-item mb-3 p-3 border rounded';
    div.innerHTML = `
        <div class="row g-3">
            <div class="col-md-6">
                <label class="form-label">Degree/Certificate*</label>
                <input type="text" class="form-control" name="educationDegree[]" required>
            </div>
            <div class="col-md-6">
                <label class="form-label">Institution*</label>
                <input type="text" class="form-control" name="educationInstitution[]" required>
            </div>
            <div class="col-md-6">
                <label class="form-label">Start Date*</label>
                <input type="month" class="form-control" name="educationStartDate[]" required>
            </div>
            <div class="col-md-6">
                <label class="form-label">End Date (or Current)</label>
                <input type="month" class="form-control" name="educationEndDate[]">
                <div class="form-check mt-2">
                    <input class="form-check-input current-education" type="checkbox" id="currentEducation${index}" data-index="${index}">
                    <label class="form-check-label" for="currentEducation${index}">Current Education</label>
                </div>
            </div>
            <div class="col-12">
                <label class="form-label">Description</label>
                <textarea class="form-control" name="educationDescription[]" rows="3"></textarea>
            </div>
        </div>
        <span class="remove-item"><i class="fas fa-times-circle"></i></span>
    `;
    return div;
}