<template>
    <div class='header'>
        <div class="logo">
            <!--img src="../../public/img/logo.png" alt=""-->
            <h1>教务管理系统</h1>
        </div>
    </div>
</template>

<style lang='scss'>
.header {
    margin: 20px auto;
    text-align: center;
    .logo {
        img {
            width: 200px;
            height: 200px;
        }
    }
    p {
        text-indent: 20em;
    }
}
</style>


<script>
export default {
    name: 'LoginHeader'
}
</script>