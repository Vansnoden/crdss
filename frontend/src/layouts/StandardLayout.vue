<template>
    <v-layout>
        <v-container>
            <Header/>
                <v-main class="main-content">
                    <slot name="content"></slot>
                </v-main>
            <Footer/>
        </v-container>
    </v-layout>
</template>

<script setup>
import { deleteCookie } from "@/plugins/cookies";
import { useRoute, useRouter } from "vue-router";
import Header from '@/components/common/Header.vue';
import Footer from '@/components/common/Footer.vue';

const route = useRoute();
const router = useRouter();

const logout = () => {
    deleteCookie("token");
    router.push('/auth/login');
}

</script>


<style lang="scss" scoped>
.main-content{
    min-height: 80vh!important;
    overflow-y: scroll!important;
}

</style>