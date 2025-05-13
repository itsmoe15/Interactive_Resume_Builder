document.addEventListener('DOMContentLoaded', function() {
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