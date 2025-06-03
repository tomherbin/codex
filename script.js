// Animations et interactions de la page

document.addEventListener('DOMContentLoaded', function() {
    // Mettre à jour l'année du footer
    const footerYear = document.querySelector('footer p');
    const currentYear = new Date().getFullYear();
    footerYear.innerHTML = footerYear.innerHTML.replace('2025', currentYear);

    // Intersection Observer pour les effets d'apparition
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });

    // FAQ toggle
    document.querySelectorAll('.faq-item button').forEach(btn => {
        btn.addEventListener('click', () => {
            const content = btn.nextElementSibling;
            const isOpen = !content.classList.contains('hidden');
            content.classList.toggle('hidden');
            btn.classList.toggle('open');
            btn.querySelector('.arrow').textContent = isOpen ? '+' : '-';
        });
    });

    console.log('Page de coaching chargée');
});
