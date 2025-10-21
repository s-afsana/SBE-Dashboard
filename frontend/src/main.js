import './assets/styles.css'              // your old styles.css (moved here)
import { createApp } from 'vue'
import App from './App.vue'

// Mount a minimal Vue app (it can be empty for now)
createApp(App).mount('#app')

// Keep your legacy dashboard JS running exactly as before
window.addEventListener('DOMContentLoaded', () => {
  import('./legacy.js').catch(e => console.warn('legacy.js not loaded:', e))
})