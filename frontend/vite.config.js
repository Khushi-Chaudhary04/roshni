import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],

  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'https://roshni-backend-2-1q5y.onrender.com',
        changeOrigin: true,
      },
    },
  },

  preview: {
    host: true,
    allowedHosts: ['roshni-frontend.onrender.com']
  }
})
