<template>
    <StandardLayout>
        <template v-slot:content>
            <v-container class="predictCtn">
                <v-row>
                    <v-col cols="12" md="12" sm="12" class="p-2">
                        <h3 class="center-content">
                            Welcome to the prediction page
                        </h3>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-select
                            v-model="selectedCrops"
                            :items="demoCrops"
                            label="Select the other crops available to you at your location to rotate with the Potatoe crop"
                            multiple
                            persistent-hint
                            required
                        ></v-select>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12" md="6" sm="12">
                        <span class="secHeader">Configure yearly rotation span period</span>
                        <div class="customInput">
                            <label for="start_year">Start Year</label>
                            <input v-model="startYear" type="number" id="start_year" name="start_year" required="true">
                        </div>
                        <div class="customInput">
                            <label for="end_year">End Year</label>
                            <input v-model="endYear" type="number" id="end_year" name="end_year" required="true">
                        </div>
                    </v-col>
                    <v-col cols="12" md="6" sm="12">
                        <span class="secHeader">Configure location</span>
                        <div class="customInput">
                            <label for="lat">Latitude</label>
                            <input v-model="latitude" type="number" id="lat" name="lat" required="true">
                        </div>
                        <div class="customInput">
                            <label for="lon">Longitude</label>
                            <input v-model="longitude" type="number" id="lon" name="lon" required="true">
                        </div>
                        <!-- <v-select
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
                        ></v-select> -->
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12" md="6" sm="12">
                        <v-btn @click="submitInputs()" color="primary">get rotation plan</v-btn>
                    </v-col>
                    <v-col cols="12" md="6" sm="12">
                        <v-btn @click="reset()" color="warning">Reset</v-btn>
                    </v-col>
                </v-row>
                <v-divider class="mb-3 mt-4"></v-divider>
                <v-row>
                    <v-col v-if="predictionStore.getPrediction">
                        <v-data-table :items="predictionStore.getPrediction"></v-data-table>
                    </v-col>
                    <v-col v-else>
                        Computing ...
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
import { baseData } from '@/components/constants';


const systemStore = useSystemStore();
const predictionStore = userPredictionStore()
const demoCrops = baseData.crops;
const demoCountries = {
    'India':['Mumbai', 'Kolkata', 'Bengaluru', 'Chennai'],
    'Sri Lanka':['Colombo', 'Galle', 'Jaffna']
};

const selectedCrops = ref([]);
const startYear = ref(0);
const endYear = ref(0);
const longitude = ref(0);
const latitude = ref(0);
const valid = ref(false);
const errors = ref(false);


const submitInputs = async () => {
    if(selectedCrops.value.length !== 0 
    && longitude.value 
    && latitude.value 
    && startYear.value 
    && endYear.value){
        errors.value = false;
        await predictionStore.pullPrediction(selectedCrops.value, 
            latitude.value, longitude.value, startYear.value, 
            endYear.value);
    }else{
        errors.value = true;
    }
}

const reset = () => {
    selectedCrops.value = [];
    startYear.value = 0;
    endYear.value = 0;
    longitude.value = 0;
    latitude.value = 0;
    valid.value = false;
    errors.value = false;
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
        /*text-decoration: underline;*/
        margin-bottom: 1em;
    }
    .errors{
        color: red;
        font-size: 1.1rem;
        font-weight: bolder;
    }
}
</style>