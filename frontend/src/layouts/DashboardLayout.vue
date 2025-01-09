<template>
    <v-layout>
        <v-navigation-drawer persistent permanent>
            <v-list-item title="CRDSS" subtitle="Crop Rotation DSS"></v-list-item>
            <v-divider></v-divider>
            <slot name="menu"></slot>
            <v-spacer></v-spacer>
            <v-divider></v-divider>
            <v-list-item link title="Logout" @click="logout"></v-list-item>
        </v-navigation-drawer>
        <v-main class="main-content">
            <slot name="content"></slot>
        </v-main>
    </v-layout>
</template>

<script setup>
import { deleteCookie } from "@/plugins/cookies";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const logout = () => {
    deleteCookie("token");
    router.push('/auth/login');
}

</script>


<style lang="scss" scoped>
.main-content{
    height: 100vh!important;
    overflow-y: scroll!important;
}

</style>