<template>
  <div>
    <el-container>
      <el-header style>
        <span
          class="mySystem"
          style="
              font-size: 30px; 
              font-weight: bold; 
              float: left;
              "
        >高校管理系统</span>
        <a @click="loginout" style="float: right; text-decoration: none; color: #552299">安全退出</a>
        <span style="float: right;margin-right: 15px">
          欢迎
          <i>{{username}}</i> 使用
        </span>
      </el-header>
    </el-container>
    <el-container>
      <el-aside width="260px" height="100%" style="background-color: #B3C0D1">
        <!-- <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
                    <el-radio-button :label="false">展开</el-radio-button>
                    <el-radio-button :label="true">收起</el-radio-button>
        </el-radio-group>-->
        <el-menu
          :default-active="this.$route.path"
          :router="true"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          :collapse="isCollapse"
          style="background-color: #B3C0D1"
        >
          <el-submenu index="8">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">首页</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                v-for="(item,i) in stList"
                :key="i"
                :index="item.name"
              >{{ item.navItem }}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="0">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">账户信息管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                v-for="(item,i) in grList"
                :key="i"
                :index="item.name"
              >{{ item.navItem }}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">校区信息管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                v-for="(item,i) in xqList"
                :key="i"
                :index="item.name"
              >{{ item.navItem }}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">专业信息管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                v-for="(item,i) in zyList"
                :key="i"
                :index="item.name"
              >{{ item.navItem }}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">班级信息管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                v-for="(item,i) in bjList"
                :key="i"
                :index="item.name"
              >{{ item.navItem }}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="4">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">学生信息管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                v-for="(item,i) in xsxxList"
                :key="i"
                :index="item.name"
              >{{ item.navItem }}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="5">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">学籍异动管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                v-for="(item,i) in xjxxList"
                :key="i"
                :index="item.name"
              >{{ item.navItem }}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="6">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">教师信息管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                v-for="(item,i) in jsxxList"
                :key="i"
                :index="item.name"
              >{{ item.navItem }}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="7">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">课程信息管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                v-for="(item,i) in kcList"
                :key="i"
                :index="item.name"
              >{{ item.navItem }}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>


<style lang='scss'>
@import "../static/css/base.scss";
.mySystem {
  @include fontOne;
}
body,
html {
  height: 100%;
  .el-container:nth-child(1) {
  }
  .el-container:nth-child(2) {
    height: 875px;
    .el-aside {
      li {
        .el-menu-item-group {
          background-color: #cadee2;
        }
      }
    }
  }
}
.el-header {
  background-color: #b3c0d1;
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
      username: "",
      isCollapse: false,
      xqList: [{ name: "/manager/campusManager", navItem: "校区信息管理" }],
      zyList: [{ name: "/manager/majorManager", navItem: "专业信息管理" }],
      bjList: [{ name: "/manager/classMsgManager", navItem: "班级信息管理" }],
      xsxxList: [{ name: "/manager/studentMsgMange", navItem: "学生信息管理" }],
      xjxxList: [
        { name: "/manager/adjustmentManager", navItem: "学籍异动管理" }
      ],
      jsxxList: [
        { name: "/manager/teacherMsgManage", navItem: "教师信息管理" }
      ],
      kcList: [
        { name: "/manager/courseManager", navItem: "课程信息管理" },
        { name: "/manager/lectureManager", navItem: "教师开课管理" },
        { name: "/manager/selectionManager", navItem: "学生选课管理" }
      ],
      grList: [{ name: "/manager/userManage", navItem: "账户信息管理" }],
      stList: [{ name: "/manager/start", navItem: "首页" }]
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    loginout() {
      // this.$router.push("/login");
      // window.localStorage.removeItem("manInfo");
      this.$http.get("/api/logout").then(res => {
        console.log(res.data);
        this.$router.push("/login");
      });
    }
  },
  created: function() {
    console.log("页面加载");
    var username = JSON.parse(window.localStorage.manInfo).username;
    this.username = username;
  }
};
</script>