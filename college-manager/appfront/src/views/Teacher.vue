<template>
    <div>
        <el-container>
            <el-header style="">
              <span style='font-size: 30px; font-weight: bold; float: left' class='mySystem'>教务管理系统</span>
              <a @click="loginout" style='float: right; text-decoration: none; color: #552299'>安全退出</a>
              <span style='float: right; margin-right: 15px'>欢迎 <i>{{username}}</i> 使用</span>
            </el-header>
        </el-container>
        <el-container>
            <el-aside width="260px" height='100%' style="background-color: #B3C0D1">
                <el-menu :default-active="this.$route.path" :router="true" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse"  style="background-color: #B3C0D1">
                    <el-submenu index="0">
                        <template slot="title">
                            <i class="el-icon-location"></i>
                            <span slot="title">首页</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item v-for="(item,i) in stList" :key="i" :index="item.name">{{ item.navItem }}</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                    <el-submenu index="1">
                        <template slot="title">
                            <i class="el-icon-location"></i>
                            <span slot="title">个人信息管理</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item v-for="(item,i) in xxList" :key="i" :index="item.name">{{ item.navItem }}</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                    <el-submenu index="2">
                        <template slot="title">
                            <i class="el-icon-location"></i>
                            <span slot="title">开课管理</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item v-for="(item,i) in kkList" :key="i" :index="item.name">{{ item.navItem }}</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                </el-menu>
            </el-aside>
            <el-main><el-main><router-view></router-view></el-main></el-main>
        </el-container>
    </div>
</template>


<style lang='scss'>
  @import "../static/css/base.scss";
  .mySystem {
    @include fontOne;
  }
  body, html{
    height: 100%;
    .el-container:nth-child(1) {
    }
    .el-container:nth-child(2) {
        height: 875px;
       .el-aside  {
        li {
            .el-menu-item-group {
                background-color: #CADEE2;
            }
        }
      }
    }
  }
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  .title {
    font-size: 20px;
  }
 .el-submenu__title {
    font-size: 20px;
  }
  .el-menu-item-group__title {
    font-size: 18px;
  }

</style>


<script>
  export default {
    data() {

        return {
            username: '',
            isCollapse: false,
            stList: [
                {name:'/teacher/start',navItem:'首页'},
            ],
            xxList: [
                {name:'/teacher/teaMessage',navItem:'个人信息管理'},
            ],
            kkList: [
                {name:'/teacher/startCourse', navItem:'开课管理'}
            ]
        }
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      loginout(){
        // window.localStorage.removeItem("teaInfo")
        this.$http.get('/api/logout')
          .then((res)=>{
            console.log(res.data);
            this.$router.push('/login')

          })
      },
    },
    created: function() {
        console.log('页面加载')
        var user = JSON.parse(window.localStorage['id'])
        this.username = user
    }
};
</script>