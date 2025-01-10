<template>

    <v-main class="pt-4 bg-blue h-100 loginCtn">
        <v-card class="mx-auto" width="400">
            <v-card-title>
                <span class="font-weight-black">Log In</span>
            </v-card-title>
            <v-card-text class="pt-4">
                <v-row>
                    <v-col cols="12" md="12">
                        <v-text-field
                        v-model="username"
                        append-icon="mdi-account"
                        type="text"
                        label="Username"
                        :rules="[rules.required]"
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12" md="12">
                        <v-text-field
                            v-model="password"
                            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                            :rules="[rules.required, rules.min]"
                            :type="show ? 'text' : 'password'"
                            hint="At least 5 characters"
                            label="Password"
                            @click:append="show = !show"
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row align="center">
                    <v-col cols="12" md="6" sm="12">
                        <v-btn class="bg-primary" @click="loginUser">Log In</v-btn>
                    </v-col>
                </v-row>
                <v-row>
                    <span class="text-danger">
                        {{ error }}
                    </span>
                    <span class="text-success">
                        {{ success }}
                    </span>
                </v-row>
            </v-card-text>
        </v-card>
    </v-main>
    
</template>

<script setup>
import { ref } from 'vue';
import { AUTH_URL } from '../constants';
import { deleteCookie, setCookie } from '@/plugins/cookies';
import { useRoute, useRouter } from "vue-router";
import { onMounted } from 'vue';
import { useSystemStore } from '@/stores/stores';

const systemStore = useSystemStore();
const route = useRoute();
const router = useRouter();
const show = ref(false);
const error = ref("");
const success = ref("");
const token = ref(null);
const password = ref(null);
const username = ref(null);
const rules = {
    required: value => !!value || 'Required.',
    min: v => v.length >= 4 || 'Min 5 characters',
}

const loginUser = async ()=>{
    if(username.value && password.value){
        let formData = new FormData();
        formData.append('username', username.value);
        formData.append('password', password.value);
        await fetch(AUTH_URL, {
            method: 'POST',
            body: formData
        }).then((res)=>{
            return res.json()
        }).then((data) => {
            if(!data.access_token){
                error.value = data.detail;
                success.value = "";
                return false;
            }else{
                token.value = data;
                success.value = "successfuly logged in";
                error.value = "";
                deleteCookie("token");
                setCookie("token", token.value.token_type + " " +token.value.access_token, 1);
                return true;
            }
        }).then((isAuth)=>{
            if(isAuth){
                router.push({ 'path': '/'});
            }
        })
    }
}

onMounted(()=>{
    document.title = `Log In`;
    systemStore.updateFavicon();
})
</script>

<style scoped lang="scss">
.loginCtn{
    .text-danger{
        color: red
    }
    .text-success{
        color:green
    }
}
</style>
  