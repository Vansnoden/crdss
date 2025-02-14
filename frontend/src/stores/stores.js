import { defineStore } from 'pinia';
import { getCookie } from '@/plugins/cookies';
import { PREDICTION_URL } from '@/components/constants';



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


export const userPredictionStore = defineStore('prediction', {
    state: () => ({
        prediction: [],
        loading: true
    }),
    getters: {
        isLoading: (state) => state.loading,
        getPrediction: (state) => state.prediction
    },
    actions: {
        async pullPrediction (crops, lat, lon, startYear, endYear){
            const data = JSON.stringify({
                "crops": ""+crops,
                "lat": ""+lat,
                "lon": ""+lon,
                "startYear": ""+startYear,
                "endYear": ""+endYear
            })
            console.log(data);

            const response = await fetch(PREDICTION_URL, {
                method: 'POST',
                headers: {
                    "Authorization": getCookie("token"),
                    "Content-type": "application/json"
                },
                body: data
            })
            const res = await response.json();
            this.prediction = res.data;
        }
    }

})