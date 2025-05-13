document.addEventListener('DOMContentLoaded', function() {
    const themeSwitch = document.querySelector('.theme-switch__checkbox');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    // تحميل التفضيل المحفوظ
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        themeSwitch.checked = savedTheme === 'dark';
        document.body.classList.toggle('dark-theme', savedTheme === 'dark');
    } else {
        // إذا لم يكن هناك تفضيل محفوظ، استخدم تفضيل النظام
        const initialTheme = prefersDarkScheme.matches ? 'dark' : 'light';
        themeSwitch.checked = prefersDarkScheme.matches;
        document.body.classList.toggle('dark-theme', prefersDarkScheme.matches);
        localStorage.setItem('theme', initialTheme);
    }
    
    // تغيير الوضع عند النقر على الزر
    themeSwitch.addEventListener('change', function() {
        const newTheme = this.checked ? 'dark' : 'light';
        document.body.classList.toggle('dark-theme', this.checked);
        localStorage.setItem('theme', newTheme);
        
        // إضافة تأثير سلس للتبديل
        document.body.style.transition = 'background-color 0.5s ease, color 0.5s ease';
        setTimeout(() => {
            document.body.style.transition = '';
        }, 500);
    });
    
    // متابعة تغييرات نظام التشغيل (فقط إذا لم يكن هناك تفضيل محفوظ)
    prefersDarkScheme.addEventListener('change', e => {
        if (!localStorage.getItem('theme')) {
            themeSwitch.checked = e.matches;
            document.body.classList.toggle('dark-theme', e.matches);
        }
    });
});