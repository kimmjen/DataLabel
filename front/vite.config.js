// FILE: vite.config.js

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { quasar, transformAssetUrls } from '@quasar/vite-plugin'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({
      template: { transformAssetUrls }
    }),

    // @quasar/plugin-vite options list:
    // https://github.com/quasarframework/quasar/blob/dev/vite-plugin/index.d.ts
    quasar({
      sassVariables: 'src/assets/css/quasar-variables.sass'
    })
  ],
  server: {
    proxy: {
      // 프록시 설정
      '/api': {
        target: 'http://localhost:8000',  // FastAPI 서버 주소
        changeOrigin: true,               // CORS 헤더를 변경하여 프록시 처리
        secure: false                     // HTTPS가 아닌 경우 true로 설정
      }
    }
  }
})
