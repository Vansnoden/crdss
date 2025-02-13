<template>
    <StandardLayout>
        <template v-slot:content>
            <v-container class="predictCtn">
                <v-row>
                    <v-col cols="12" md="12" sm="12" class="p-2">
                        <p class="center-content">
                            Welcome to the prediction page
                        </p>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-select
                            v-model="selectedCrops"
                            :items="demoCrops"
                            label="Select crops to rotate"
                            multiple
                            persistent-hint
                            required
                        ></v-select>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12" md="6" sm="12">
                        <span class="secHeader">Configure Period</span>
                        <div class="customInput">
                            <label for="start_date">Start Date</label>
                            <input v-model="startDate" type="date" id="start_date" name="start_date" required="true">
                        </div>
                        <div class="customInput">
                            <label for="end_date">End Date</label>
                            <input v-model="endDate" type="date" id="end_date" name="end_date" required="true">
                        </div>
                    </v-col>
                    <v-col cols="12" md="6" sm="12">
                        <span class="secHeader">Configure location</span>
                        <v-select
                            class="pt4"
                            v-model="country"
                            label="Select country"
                            :items="Object.getOwnPropertyNames(demoCountries)"
                            required
                        ></v-select>
                        <v-select
                            v-model="region"
                            label="Select country area"
                            :items="demoCountries[country]"
                            required
                        ></v-select>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12" md="6" sm="12">
                        <v-btn @click="submitInputs()">get rotation plan</v-btn>
                    </v-col>
                </v-row>
                <v-divider class="mb-3 mt-4"></v-divider>
                <v-row>
                    <v-col>
                        <v-data-table :items="predictionStore.getPrediction"></v-data-table>
                    </v-col>
                </v-row>
                <v-row v-if="errors" class="errors center-content">
                    Please you should provide all parameters...
                </v-row>
            </v-container>
        </template>
    </StandardLayout>
</template>

<script setup>
import StandardLayout from '@/layouts/StandardLayout.vue';
import { useSystemStore, userPredictionStore } from '@/stores/stores';
import { onMounted, ref } from 'vue';


const systemStore = useSystemStore();
const predictionStore = userPredictionStore()
const demoCrops = ['Lettuce', 'Spinach', 'Wheat', 'Beans', 'Potatoes', 'Clover', 'Rye'];
const demoCountries = {
    'India':['Mumbai', 'Kolkata', 'Bengaluru', 'Chennai'],
    'Sri Lanka':['Colombo', 'Galle', 'Jaffna']
};

const selectedCrops = ref([]);
const country = ref("");
const region = ref("");
const startDate = ref("");
const endDate = ref("");
const valid = ref(false);
const errors = ref(false);


const submitInputs = async () => {
    if(selectedCrops.value.length !== 0 
    && country.value 
    && region.value 
    && startDate.value 
    && endDate.value){
        errors.value = false;
        await predictionStore.pullPrediction(selectedCrops.value, 
            country.value, region.value, startDate.value.split("-")[0], 
            endDate.value.split("-")[0]);
    }else{
        errors.value = true;
    }
}


onMounted(() => {
    document.title = `Prediction`;
    systemStore.updateFavicon();
})

</script>

<style lang="scss">
.predictCtn{
    text-align: justify;
    .center-content{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: row;
    }
    .customInput{
        margin-bottom: 1em;
        label{
            display: block;
        }
        input{
            border: 1px solid rgb(187, 187, 187);
            width: 100%;
            padding: 0.5em;
            border-radius: 5px;
        }
    }
    .pt4{
        margin-top: 2.5em;
    }
    .secHeader{
        display: block;
        font-size: 1.2rem;
        font-weight: bold;
        text-decoration: underline;
        margin-bottom: 1em;
    }
    .errors{
        color: red;
        font-size: 1.1rem;
        font-weight: bolder;
    }
}
</style>