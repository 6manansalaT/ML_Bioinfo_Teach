(() => {
    // Add event listener to capture keyboard events
    window.parent.document.addEventListener('keydown', function(e) {
        console.log('Key pressed:', e.key);
        Streamlit.setComponentValue(e.key);
    });
    
    // Initialize component
    Streamlit.setComponentReady();
})();