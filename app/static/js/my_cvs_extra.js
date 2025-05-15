function filterCVs(style) {
    document.querySelectorAll('.cv-card').forEach(function(card) {
        if (style === 'All' || card.getAttribute('data-style') === style) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
    document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById('btn-' + style).classList.add('active');
}
// Set default filter to All
filterCVs('All'); 