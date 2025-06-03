// Wait for DOM to be loaded
document.addEventListener('DOMContentLoaded', function() {
    // Display current year in footer
    const footerYear = document.querySelector('footer p');
    const currentYear = new Date().getFullYear();
    footerYear.innerHTML = footerYear.innerHTML.replace('2025', currentYear);
    
    // Add a simple animation effect to the hero section
    const hero = document.querySelector('.hero');
    setTimeout(() => {
        hero.style.transition = 'all 0.5s ease';
        hero.style.transform = 'translateY(0)';
        hero.style.opacity = '1';
    }, 100);
    hero.style.transform = 'translateY(20px)';
    hero.style.opacity = '0';
    
    // Log a message to console
    console.log('Le site Codex est chargé et prêt !');
});
