<template>
  <div>
    <!-- <div style='height:90px'>
      <span class='font'>欢迎进入账号信息管理模块</span>
      <p class="text">小贴士：定期清理无效账户，能够提升系统效率哦</p>  
    </div>-->
    <el-row>
      <div>
        <el-form
          :inline="true"
          :model="form"
          :rules="searchRules"
          ref="form"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-row type="flex" class="row-bg">
            <el-col :span="6">
              <div class="grid-content bg-purple-light">
                <el-form-item label="学工号" prop="id">
                  <el-input v-model="form.id"></el-input>
                </el-form-item>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple-light">
                <el-form-item label="类型" prop="category">
                  <el-select v-model="form.category" placeholder="请选择">
                    <el-option label="教师" value="教师" autocomplete="off"></el-option>
                    <el-option label="学生" value="学生" autocomplete="off"></el-option>
                  </el-select>
                </el-form-item>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content"></div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content"></div>
            </el-col>
            <el-col :span="3">
              <el-button type="warning" plain @click="mysearchData()">搜索</el-button>
            </el-col>
            <el-col :span="3">
              <el-button type="danger" plain @click="getAllData()">刷新</el-button>
            </el-col>
          </el-row>
        </el-form>
      </div>
    </el-row>
    <el-table :data="tableData" stripe style="width: 100%">
      <el-table-column prop="id" label="账户名"></el-table-column>
      <el-table-column prop="password" label="密码"></el-table-column>
      <el-table-column prop="category" label="类型"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="primary" @click="editData(scope.$index)">修改</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog title="填写你的信息" :visible.sync="dialogFormVisible" style="height: 100%">
      <el-form :model="form" :rules="rules" ref="form">
        <el-form-item label="账户名" prop="id" autocomplete="off">
          <el-input v-model="form.id" autocomplete="off" :disabled="isEdit"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="new">
          <el-input v-model="form.new" autocomplete="off"></el-input>
        </el-form-item>
        <!--  <el-form-item label="类型" prop="category">
          <el-input v-model="form.category" autocomplete="off"></el-input>
        </el-form-item>-->
        <el-form-item label="类型" prop="category">
          <el-select style="width: 50%" v-model="form.category">
            <el-option label="学生" value="student" autocomplete="off"></el-option>
            <el-option label="教师" value="teacher" autocomplete="off"></el-option>
            <!-- <el-option label="教学管理者" value="manager" autocomplete="off"></el-option> -->
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitFrom">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<style lang='scss'>
@import "../../static/css/base.scss";
.font {
  @include fontTwo();
}
.text {
  @include fontThree();
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
<script>
export default {
  name: "index",
  data() {
    return {
      dialogVisible: false,
      tableData: [],
      dialogFormVisible: false,
      isEdit: false, //是否修改
      editId: "",
      delId: "",
      form: {
        id: "",
        new: "",
        password: "",
        category: ""
      },
      searchRules: {},
      rules: {
        id: [
          { required: true, message: "必填", trigger: "blur" },
          { min: 3, max: 20, message: "长度在 3 到 20 个字符", trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    // 驼峰转换下划线
    toLine(name) {
      return name.replace(/([A-Z])/g, "_$1").toLowerCase();
    },

    simplify(obj) {
      let newobj = new Object();
      for (let key in obj) {
        if (obj[key]) newobj[key] = obj[key];
      }
      return newobj;
    },

    sendGetRequest(url, opt = {}) {
      var _this = this;
      this.$http
        .get(url, opt)
        .then(function(res) {
          console.log(res);
          if (url === "/api/teacher/get") {
            _this.tableData = [];
            for (let i = 0; i < res.data["list"].length; i++) {
              let newform = { id: res.data["list"][i]["id"], category: "教师" };
              _this.tableData.push(newform);
            }
          } else if (url === "/api/student/get") {
            _this.tableData = [];
            for (let i = 0; i < res.data["list"].length; i++) {
              let newform = { id: res.data["list"][i]["id"], category: "教师" };
              _this.tableData.push(newform);
            }
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    sendPostRequest(url, opt = {}) {
      var _this = this;
      console.log(opt);
      this.$http
        .post(url, JSON.stringify(opt), { emulateJSON: true })
        .then(function(res) {
          console.log(res);
          var resbody = JSON.parse(res.bodyText);

          if (url === "/api/password/admin_mod") {
            if (resbody["code"] == 0) {
              _this.$message.error("修改账户信息失败：" + resbody["msg"]);
            }
          } else {
            _this.$message.error("invalid request");
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    submitFrom() {
      const that = this;
      this.$refs["form"].validate(valid => {
        if (valid) {
          if (that.isEdit) {
            let opt = that.form;
            delete opt.category;
            delete opt.password;
            that.sendPostRequest("/api/password/admin_mod", opt);
          }
          that.dialogFormVisible = false;
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },

    // 请求所有数据
    getAllData() {
      var _this = this;
      this.$http
        .get("/api/teacher/get")
        .then(function(res) {
          var resbody = JSON.parse(res.bodyText);
          if (resbody["code"] == 0) {
            _this.$message.error("查询用户失败");
          } else {
            _this.tableData = [];
            for (let i = 0; i < res.data["list"].length; i++) {
              let newform = { id: res.data["list"][i]["id"], category: "教师" };
              _this.tableData.push(newform);
            }
          }
        })
        .catch(function(error) {
          console.log(error);
        });
      this.$http
        .get("/api/student/get")
        .then(function(res) {
          var resbody = JSON.parse(res.bodyText);
          if (resbody["code"] == 0) {
            _this.$message.error("查询用户失败");
          } else {
            for (let i = 0; i < res.data["list"].length; i++) {
              let newform = { id: res.data["list"][i]["id"], category: "学生" };
              _this.tableData.push(newform);
            }
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    editData(index) {
      const selfData = this.tableData[index];
      this.editIndex = index;
      this.editId = selfData.id;
      this.dialogFormVisible = true;
      this.isEdit = true;
      this.form.id = selfData.id;
      this.form.password = selfData.password;
    },

    openDialog(index) {
      this.delId = this.tableData[index]["id"];
      this.delIndex = index;
      this.dialogVisible = true;
    },

    mysearchData() {
      console.log(this.form);
      switch (this.form.category) {
        case "学生":
          this.sendGetRequest("/api/student/get", {
            params: this.simplify(this.form)
          });
          break;
        case "教师":
          this.sendGetRequest("/api/teacher/get", {
            params: this.simplify(this.form)
          });
          break;
        default:
          var _this = this;
          this.$http
            .get("/api/teacher/get", {
              params: this.simplify(this.form)
            })
            .then(function(res) {
              var resbody = JSON.parse(res.bodyText);
              if (resbody["code"] == 0) {
                _this.$message.error("查询用户失败");
              } else {
                _this.tableData = [];
                for (let i = 0; i < res.data["list"].length; i++) {
                  let newform = {
                    id: res.data["list"][i]["id"],
                    category: "教师"
                  };
                  _this.tableData.push(newform);
                }
              }
            })
            .catch(function(error) {
              console.log(error);
            });
          this.$http
            .get("/api/student/get", {
              params: this.simplify(this.form)
            })
            .then(function(res) {
              var resbody = JSON.parse(res.bodyText);
              if (resbody["code"] == 0) {
                _this.$message.error("查询用户失败");
              } else {
                for (let i = 0; i < res.data["list"].length; i++) {
                  let newform = {
                    id: res.data["list"][i]["id"],
                    category: "学生"
                  };
                  _this.tableData.push(newform);
                }
              }
            })
            .catch(function(error) {
              console.log(error);
            });
          break;
      }
    },

    reload() {
      this.isRouterAlive = false; //先关闭，
      this.$nextTick(function() {
        this.isRouterAlive = true; //再打开
      });
    },

    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },

    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  },

  watch: {
    dialogFormVisible() {
      if (!this.dialogFormVisible) this.isEdit = false;
    }
  },

  mounted: function() {
    // 组件创建时候去获取所有的用户数据
    this.getAllData();
  }
};
</script>