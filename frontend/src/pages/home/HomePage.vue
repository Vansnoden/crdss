<template>
    <StandardLayout>
        <template v-slot:content>
            <v-container class="homeCtn">
                <v-row>
                    <v-col cols="12" md="6" sm="12" class="p-2">
                        <v-card class="center-content">
                            <img src="/img/bg_potatoes.png" class="homeImg"/>
                        </v-card>
                    </v-col>
                    <v-col cols="12" md="6" sm="12" class="p-2">
                        <v-card class="center-content">
                            <img src="/img/crop_rotation.webp" class="homeImg"/>
                        </v-card>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12" md="6" sm="12" xs="12" class="p-2">
                        <p>
                            Crop rotation is a critical agricultural practice that significantly impacts 
                            the health and productivity of potato crops. By alternating potatoes with 
                            other crop varieties, farmers can prevent the buildup of soil-borne pests 
                            and diseases, such as nematodes and late blight, which can devastate potato 
                            yields over time. Moreover, rotation helps maintain soil fertility by 
                            diversifying nutrient demands, reducing the depletion of specific nutrients 
                            that potatoes heavily rely on, such as potassium and nitrogen. Incorporating 
                            crops like legumes into the rotation can naturally enrich the soil with nitrogen, 
                            minimizing the need for synthetic fertilizers. This practice not only ensures a 
                            healthier potato crop but also promotes sustainable farming by improving soil 
                            structure and reducing erosion, making the land more resilient to environmental 
                            stresses.
                        </p>
                    </v-col>
                    <v-col cols="12" md="6" sm="12"  xs="12" class="p-2">
                        <p>
                            Predicting the optimal rotation pattern is crucial for maximizing potato yield 
                            while minimizing risks. Effective rotation requires understanding the 
                            interactions between different crops, soil conditions, and environmental 
                            factors. Advanced tools such as predictive modeling and machine learning 
                            are emerging to assist farmers in determining the most beneficial sequences. 
                            These tools analyze historical yield data, soil quality metrics, and local 
                            climate patterns to recommend tailored rotation strategies. For instance, 
                            alternating potatoes with brassicas or cereals might optimize nutrient cycling 
                            and suppress pests in a specific region. By leveraging predictive tools, 
                            farmers can fine-tune their crop rotations, ensuring sustainable practices 
                            and achieving higher yields, ultimately benefiting food security and economic 
                            stability.
                        </p>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12" md="12" sm="12" class="center-content mt-4">
                        <v-btn primary @click="goToPrediction()">make prediction</v-btn>
                    </v-col>
                </v-row>
            </v-container>
        </template>
    </StandardLayout>
</template>


<script setup>;
import StandardLayout from '@/layouts/StandardLayout.vue';
import { useSystemStore } from '@/stores/stores';
import { onMounted } from 'vue';
import { useRoute, useRouter } from "vue-router";


const route = useRoute();
const router = useRouter();
const systemStore = useSystemStore();
const goToPrediction = () => {
    router.push('/prediction');
}

onMounted(() => {
    document.title = `Home`;
    systemStore.updateFavicon();
})

</script>


<style lang="scss">
.homeCtn{
    text-align: justify;
    .homeImg{
        height: 30vh;
        width: auto;
    }
    .center-content{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: row;
    }
    
}
</style>