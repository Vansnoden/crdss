<template>
    <div class="myHeader">
        <div class="logoCtn">
            <img src="/img/logo.svg" class="logo"/>
            <span>CRDSS</span>
        </div>
        <ul class="nav">
            <li>
                <a href="/">About</a>
            </li>
            <li>
                <a href="#">?</a>
            </li>
        </ul>
        <ul class="nav">
            <li v-if="isAuthenticated()">
                <v-btn @click="logout" primary>log out</v-btn>
            </li>
            <li v-else>
                <a href="/auth/login">Log In</a>
            </li>
        </ul>
    </div>
</template>


<script setup>
import { isAuthenticated } from '@/plugins/auth';
import { useRoute, useRouter } from "vue-router";
import { deleteCookie } from '@/plugins/cookies';

const route = useRoute();
const router = useRouter();

const logout = () => {
    deleteCookie("token");
    router.push({ name:'login' });
}

</script>


<style lang="scss">
.myHeader{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-direction: auto;
    border-bottom: 1px solid rgb(214, 214, 214);
    padding-bottom: 1em;
    .logoCtn{
        color: rgb(70, 70, 168);
        font-weight: bolder;
        .logo{
            height: 40px;
            width: 40px;
            color: rgb(70, 70, 168);
        }
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-direction: row;
        gap: 1em
    }
    
    .nav{
        list-style-type: none;
        li{
            display: inline-block;
            padding: 10px;
            margin-left: 1em;
            a{
                text-decoration: none;
                color: rgb(70, 70, 168);
                font-weight: bolder;
            }
        }
    }
}
</style>