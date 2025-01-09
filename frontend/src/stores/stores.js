import { defineStore } from 'pinia';
import { getCookie } from '@/plugins/cookies';



export const useSystemStore = defineStore('system', {
    state: () => ({
        favicon_url: '/favicon.png'
    }),
    getters: {
        getFaviconUrl: (state) => state.favicon_url,
    },
    actions: {
        updateFavicon(){
            let link = document.querySelector("link[rel~='icon']");
            if (!link) {
            link = document.createElement('link');
            link.rel = 'icon';
            document.head.appendChild(link);
            }
            link.href = this.favicon_url;
        }
    }
})