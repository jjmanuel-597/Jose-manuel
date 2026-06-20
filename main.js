/*==================== SCROLLREVEAL ANIMATIONS ====================*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2000,
    delay: 200,
    opacity: 0,
    easing: 'ease-in-out',
});

sr.reveal('.home__container', {});
sr.reveal('.home__social', { origin: 'left', delay: 400 });
sr.reveal('.home__img', { origin: 'right', delay: 600 });

sr.reveal('.about__container', { interval: 200 });
sr.reveal('.qualification__container', { interval: 300 });
sr.reveal('.skills__item', { interval: 200 });
sr.reveal('.portfolio__content', { interval: 300 });
sr.reveal('.services__content', { interval: 300 });
sr.reveal('.testimonial__content', { interval: 300 });
sr.reveal('.contact__container', { interval: 300 });
sr.reveal('.footer__container', {});

/*==================== FILTRADO DEL PORTAFOLIO (MIXITUP) ====================*/
let mixerPortfolio = mixitup('.portfolio__container', {
    selectors: {
        target: '.portfolio__content'
    },
    animation: {
        duration: 300
    }
});

const linkPortfolio = document.querySelectorAll('.portfolio__item');

function activePortfolio() {
    linkPortfolio.forEach(l => l.classList.remove('active-portfolio'));
    this.classList.add('active-portfolio');
}

linkPortfolio.forEach(l => l.addEventListener('click', activePortfolio));

/*==================== VENTANAS MODALES DE SERVICIOS ====================*/
const modalViews = document.querySelectorAll('.services__modal'),
      modalBtns = document.querySelectorAll('.services__button'),
      modalCloses = document.querySelectorAll('.services__modal-close');

let modal = function(modalClick) {
    modalViews[modalClick].classList.add('active-modal');
}

modalBtns.forEach((modalBtn, i) => {
    modalBtn.addEventListener('click', () => {
        modal(i);
    });
});

modalCloses.forEach((modalClose) => {
    modalClose.addEventListener('click', () => {
        modalViews.forEach((modalView) => {
            modalView.classList.remove('active-modal');
        });
    });
});

/*==================== CARRUSEL DE TESTIMONIOS (SWIPER) ====================*/
let swiperTestimonial = new Swiper('.testimonial__container', {
    spaceBetween: 24,
    loop: true,
    grabCursor: true,
    
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    breakpoints: {
        576: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 48,
        }
    }
});

/*==================== BARRA LATERAL ACTIVA AL HACER SCROLL ====================*/
const sections = document.querySelectorAll('section[id]');

function scrollActive() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 50;
        const sectionId = current.getAttribute('id');
        const targetLink = document.querySelector('.nav__menu a[href*=' + sectionId + ']');

        if (targetLink) {
            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                targetLink.classList.add('active-link');
            } else {
                targetLink.classList.remove('active-link');
            }
        }
    });
}
window.addEventListener('scroll', scrollActive);

/*==================== TABS CALIFICACIÓN ====================*/
const qualificationBtns = document.querySelectorAll('.qualification__button');
const qualificationData = document.querySelectorAll('.qualification__content');

qualificationBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        qualificationBtns.forEach(b => b.classList.remove('qualification__active'));
        this.classList.add('qualification__active');

        const target = this.dataset.target;

        qualificationData.forEach(content => {
            if (content.id === target) {
                content.classList.add('qualification__active');
            } else {
                content.classList.remove('qualification__active');
            }
        });
    });
});
