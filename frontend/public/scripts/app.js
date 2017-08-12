(function() {
    'use strict';

    var app = {
        isLoading: true,
        visibleCards: {},
        selectedCities: [],
        spinner: document.querySelector('.loader'),
        cardTemplate: document.querySelector('.cardTemplate'),
        container: document.querySelector('.main'),
        addDialog: document.querySelector('.dialog-container'),
        daysOfWeek: [
            'Mon',
            'Tue',
            'Wed',
            'Thu',
            'Fri',
            'Sat',
            'Sun'
        ]
    };

    /*****************************************************************************
   *
   * Event listeners for UI elements
   *
   ****************************************************************************/
    document.getElementById('butRefresh').addEventListener('click', function() {
        app.updateForecasts();
    });

    document.getElementById('butAbout').addEventListener('click', function() {
        app.toggleAddDialog(true);
    });

    document.getElementById('butBack').addEventListener('click', function() {
        app.toggleAddDialog(false);
    });

    /*****************************************************************************
   *
   * Methods to update/refresh the UI
   *
   ****************************************************************************/
    app.toggleAddDialog = function(visible) {
        if (visible) {
            app.addDialog.classList.add('dialog-container--visible');
        } else {
            app.addDialog.classList.remove('dialog-container--visible');
        }
    };

    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('./service-worker.js').then(function() {
            console.log('Service Worker Registered');
        });
        app.spinner.setAttribute('hidden', true);
    }
})();
