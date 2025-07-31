document.addEventListener('DOMContentLoaded', () => {
    const toasts = document.querySelectorAll('.toast-message');

    toasts.forEach(toast => {
        requestAnimationFrame(() => {
            toast.classList.add('show');
        });

        setTimeout(() => {
            toast.classList.remove('show');
            toast.classList.add('hide');

            setTimeout(() => toast.remove(), 300);
        }, 2500);

        toast.addEventListener('click', () => {
            toast.classList.remove('show');
            toast.classList.add('hide');

            setTimeout(() => toast.remove(), 300);
        });
    });
});