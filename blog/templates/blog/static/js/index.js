document.addEventListener('DOMContentLoaded', function() {
    const userMenuButton = document.getElementById('user-menu-button');
    const userDropdown = document.getElementById('user-dropdown');

    if (userMenuButton && userDropdown) {
        userMenuButton.addEventListener('click', function() {
            const expanded = userMenuButton.getAttribute('aria-expanded') === 'true';
            userMenuButton.setAttribute('aria-expanded', !expanded);
            userDropdown.classList.toggle('hidden');
        });

        document.addEventListener('click', function(event) {
            if (!userMenuButton.contains(event.target) && !userDropdown.contains(event.target)) {
                userMenuButton.setAttribute('aria-expanded', 'false');
                userDropdown.classList.add('hidden');
            }
        });
    }


    const preferenceChips = document.querySelectorAll('.preference-chip');
    preferenceChips.forEach(chip => {
        chip.addEventListener('click', function() {
            this.classList.toggle('active-preference');
            this.classList.toggle('bg-indigo-100');
            this.classList.toggle('text-indigo-800');
            this.classList.toggle('bg-gray-100');
            this.classList.toggle('text-gray-800');
        });
    });

    // Form validation for itinerary planner
    const itineraryForm = document.querySelector('button:contains("Buat Itinerary")');
    if (itineraryForm) {
        itineraryForm.addEventListener('click', function(e) {
            e.preventDefault();
            
            const destination = document.getElementById('destination');
            const startDate = document.getElementById('start-date');
            const endDate = document.getElementById('end-date');
            
            if (destination.value === 'Pilih Destinasi') {
                alert('Silakan pilih destinasi terlebih dahulu');
                return;
            }
            
            if (!startDate.value) {
                alert('Silakan pilih tanggal mulai');
                return;
            }
            
            if (!endDate.value) {
                alert('Silakan pilih tanggal selesai');
                return;
            }
            
            if (new Date(startDate.value) > new Date(endDate.value)) {
                alert('Tanggal mulai tidak boleh lebih besar dari tanggal selesai');
                return;
            }
            
            // If validation passes, you can submit the form here
            console.log('Form is valid, processing...');
        });
    }
});
