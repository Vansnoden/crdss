<template>
    <StandardLayout>
        <template v-slot:content>
            <v-form v-model="valid">
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
                            ></v-select>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="6" sm="12">
                            <span class="secHeader">Configure time</span>
                            <div class="customInput">
                                <label for="start_date">Start Date</label>
                                <input type="date" id="start_date" name="start_date">
                            </div>
                            <div class="customInput">
                                <label for="end_date">End Date</label>
                                <input type="date" id="end_date" name="end_date">
                            </div>
                        </v-col>
                        <v-col cols="12" md="6" sm="12">
                            <span class="secHeader">Configure location</span>
                            <v-select
                                class="pt4"
                                v-model="country"
                                label="Select country"
                                :items="Object.getOwnPropertyNames(demoCountries)"
                            ></v-select>
                            <v-select
                                label="Select country area"
                                :items="demoCountries[country]"
                            ></v-select>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="6" sm="12">
                            <v-btn>get rotation plan</v-btn>
                        </v-col>
                    </v-row>
                </v-container>
            </v-form>
            <v-container>
                <v-row>
                    <v-col>
                        <v-data-table :items="items"></v-data-table>
                    </v-col>
                </v-row>
            </v-container>
        </template>
    </StandardLayout>
</template>

<script setup>
import StandardLayout from '@/layouts/StandardLayout.vue';
import { useSystemStore } from '@/stores/stores';
import { onMounted, ref } from 'vue';


const systemStore = useSystemStore();
const demoCrops = ['Foo', 'Bar', 'Fizz', 'Buzz'];
const demoCountries = {
    'Country1':['Reg1', 'Reg2', 'Reg3'],
    'Country2':['Reg4', 'Reg5']
};
const items = [
    {
      crop: 'Potatoe',
      year: 2010
    },
    {
      crop: 'Potatoe',
      year: 2010
    },
    {
      crop: 'Potatoe',
      year: 2010
    },
    {
      crop: 'Potatoe',
      year: 2010
    },
    {
      crop: 'Potatoe',
      year: 2010
    }
]
const selectedCrops = ref([]);
const country = ref("");
const valid = ref(false);


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
}
</style>