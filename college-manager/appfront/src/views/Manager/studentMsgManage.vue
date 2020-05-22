<template>
  <div class="fillcontain">
    <el-row>
      <el-button
        type="primary"
        style="left: 10px; position: absolute;"
        @click="dialogFormVisible = true"
      >新增</el-button>
      <!--div class="searchbox" style="display: inline-block; float: right;"-->
      <el-button style="left: 700px; position: relative;" @click="show3 = !show3">展开搜索框</el-button>
      <el-button
        style="left: 700px; position: relative;"
        type="danger"
        plain
        @click="getAllData()"
      >刷新</el-button>
      <el-collapse-transition>
        <div class="search_container" v-if="show3">
          <br />
          <el-form
            :inline="true"
            :model="form"
            :rules="searchRules"
            ref="form"
            label-width="100px"
            class="demo-form-inline search-form"
          >
            <el-form-item
              label="姓名"
              prop="name"
              style="width: 20%; left: 30px; position: absolute;"
            >
              <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="学号" prop="id" style="width: 20%; position: relative;">
              <el-input v-model="form.id"></el-input>
            </el-form-item>
            <el-form-item label="出生日期" prop="birth" style="width: 20%">
              <el-input v-model="form.birth"></el-input>
            </el-form-item>
            <el-form-item label="性别" prop="gender" style="position: relative;">
              <el-radio-group v-model="form.gender">
                <el-radio label="男"></el-radio>
                <el-radio label="女"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item>
              <el-button type="warning" plain @click="mysearchData">搜索</el-button>
            </el-form-item>
          </el-form>
          <el-form
            :inline="true"
            :model="form"
            :rules="searchRules"
            ref="form"
            label-width="100px"
            class="demo-ruleForm"
          >
            <el-form-item
              label="班级代码"
              prop="class_id"
              style="width: 20%; left: 30px; position: absolute;"
            >
              <el-input v-model="form.class_id"></el-input>
            </el-form-item>
            <el-form-item
              label="班级名称"
              prop="class_name"
              style="width: 20%; left: 13px; position: relative;"
            >
              <el-input v-model="form.class_name"></el-input>
            </el-form-item>
            <el-form-item label="专业代码" prop="major_id" style="width: 20%; left: 30px;">
              <el-input v-model="form.major_id"></el-input>
            </el-form-item>
            <el-form-item label="专业名称" prop="major_name" style="width: 20%; left: 30px;">
              <el-input v-model="form.major_name"></el-input>
            </el-form-item>
          </el-form>
          <el-form
            :inline="true"
            :model="form"
            :rules="searchRules"
            ref="form"
            label-width="100px"
            class="demo-ruleForm"
          >
            <el-form-item
              label="身份证号"
              prop="person_id"
              style="width: 20%; left: 30px; position: absolute;"
            >
              <el-input v-model="form.person_id"></el-input>
            </el-form-item>
            <el-form-item label="身份证类型" prop="person_id_type" style="position: relative;">
              <el-radio-group v-model="form.person_id_type">
                <el-radio label="身份证"></el-radio>
                <el-radio label="护照"></el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item label="国籍" prop="country" style="width: 20%;">
              <el-input v-model="form.country"></el-input>
            </el-form-item>
          </el-form>
          <el-form
            :inline="true"
            :model="form"
            :rules="searchRules"
            ref="form"
            label-width="100px"
            class="demo-ruleForm"
          >
            <el-form-item
              label="入学时间"
              prop="enroll_date"
              style="width: 20%; left: 30px; position: absolute;"
            >
              <el-input v-model="form.enroll_date"></el-input>
            </el-form-item>
            <el-form-item
              label="家庭住址"
              prop="family_address"
              style="width: 20%; left: 13px; position: relative;"
            >
              <el-input v-model="form.family_address"></el-input>
            </el-form-item>
            <el-form-item label="邮编" prop="family_zipcode" style="width: 20%; position: relative;">
              <el-input v-model="form.family_zipcode"></el-input>
            </el-form-item>
          </el-form>
          <el-form
            :inline="true"
            :model="form"
            :rules="searchRules"
            ref="form"
            label-width="100px"
            class="demo-ruleForm"
          >
            <el-form-item
              label="联系电话"
              prop="family_tel"
              style="width: 20%; left: 30px; position: absolute;"
            >
              <el-input v-model="form.family_tel"></el-input>
            </el-form-item>
            <el-form-item
              label="电子邮箱"
              prop="email"
              style="width: 20%; left: 400px; position: absolute;"
            >
              <el-input v-model="form.email"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-collapse-transition>

      <!--/div-->
    </el-row>
    <el-scrollbar>
      <el-table :data="tableData" align="center">
        <el-table-column prop="id" label="学号" align="center"></el-table-column>
        <el-table-column prop="name" label="姓名" align="center"></el-table-column>
        <el-table-column label="性别" align="center">
          <template slot-scope="scope">
            <i v-if="scope.row.gender===0">男</i>
            <i v-else>女</i>
          </template>
        </el-table-column>
        <el-table-column prop="birth" label="出生日期" align="center"></el-table-column>
        <el-table-column prop="class_id" label="班级代码" align="center"></el-table-column>
        <el-table-column prop="class_name" label="班级名称" align="center"></el-table-column>
        <el-table-column prop="major_id" label="专业代码" align="center"></el-table-column>
        <el-table-column prop="major_name" label="专业名称" align="center"></el-table-column>
        <el-table-column label="身份证类型" align="center">
          <template slot-scope="scope">
            <i v-if="scope.row.person_id_type===0">身份证</i>
            <i v-else>护照</i>
          </template>
        </el-table-column>
        <el-table-column prop="person_id" label="身份证号" width="220" align="center"></el-table-column>
        <el-table-column prop="country" label="国籍" align="center"></el-table-column>
        <el-table-column prop="enroll_date" label="入学时间" align="center"></el-table-column>
        <el-table-column prop="family_address" label="家庭住址" align="center"></el-table-column>
        <el-table-column prop="family_zipcode" label="邮编" align="center"></el-table-column>
        <el-table-column prop="family_tel" label="联系电话" align="center"></el-table-column>
        <el-table-column prop="email" label="电子邮箱" align="center"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" @click="editData(scope.$index)">修改</el-button>
            <el-button type="danger" @click="openDialog(scope.$index)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-scrollbar>

    <el-dialog title="填写你的信息" :visible.sync="dialogFormVisible" style="height: 100%">
      <el-form :model="form" :rules="rules" ref="form">
        <el-form-item label="学号" prop="id" autocomplete="off">
          <el-input v-model="form.id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="name">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="gender">
          <el-select v-model="form.gender" placeholder="请选择性别">
            <el-option label="男" value="男" autocomplete="off"></el-option>
            <el-option label="女" value="女" autocomplete="off"></el-option>
          </el-select>
        </el-form-item>
        <!-- <el-form-item label="性别">
          <el-input v-model="form.sex" autocomplete="off"></el-input>
        </el-form-item>-->
        <el-form-item label="出生日期">
          <el-input v-model="form.birth" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="form.email" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item label="班级代码" prop="class_id">
          <el-input v-model="form.class_id"></el-input>
        </el-form-item>

        <el-form-item label="班级名称" prop="class_name">
          <el-input v-model="form.class_name"></el-input>
        </el-form-item>

        <el-form-item label="专业代码" prop="major_id">
          <el-input v-model="form.major_id"></el-input>
        </el-form-item>

        <el-form-item label="专业名称" prop="major_name">
          <el-input v-model="form.major_name"></el-input>
        </el-form-item>

        <el-form-item label="身份证类型" prop="person_id_type">
          <el-radio-group v-model="form.person_id_type">
            <el-radio label="身份证"></el-radio>
            <el-radio label="护照"></el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="身份证号" prop="person_id" autocomplete="off">
          <el-input v-model="form.person_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="国籍" prop="country">
          <el-input v-model="form.country"></el-input>
        </el-form-item>

        <el-form-item label="入学时间" prop="enroll_date">
          <el-input v-model="form.enroll_date"></el-input>
        </el-form-item>
        <el-form-item label="家庭住址" prop="family_address">
          <el-input v-model="form.family_address"></el-input>
        </el-form-item>
        <el-form-item label="邮编" prop="family_zipcode">
          <el-input v-model="form.family_zipcode"></el-input>
        </el-form-item>
        <el-form-item label="联系电话" prop="family_tel">
          <el-input v-model="form.family_tel"></el-input>
        </el-form-item>
        <el-form-item label="电子邮箱" prop="email">
          <el-input v-model="form.email"></el-input>
        </el-form-item>

        <!-- <el-form-item label="地址">
          <el-input v-model="form.adress" autocomplete="off"></el-input>
        </el-form-item>-->
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitFrom">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog title="提示" :visible.sync="dialogVisible" width="30%">
      <span>确定要删除信息</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="delData">确 定</el-button>
      </span>
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
.el-input {
  width: 80%;
}
.el-form-item__label {
  width: 15%;
}
.search-form {
  width: 100%;
  min-width: 750px;
  .el-form-item {
    margin-bottom: 10px !important;
    .el-date-editor {
      width: 200px;
      .el-input__inner {
        height: 36px !important;
      }
    }
  }
}

.transition-box {
  margin-bottom: 10px;
  width: 200px;
  height: 100px;
  border-radius: 4px;
  background-color: #409eff;
  text-align: center;
  color: #fff;
  padding: 40px 20px;
  box-sizing: border-box;
  margin-right: 20px;
}
.el-scrollbar .el-scrollbar__wrap .el-scrollbar__view {
  white-space: nowrap;
}
</style>

<script>
export default {
  name: "index",
  data() {
    return {
      dialogVisible: false,
      tableData: [], //以数组的形式存储所有信息，每条信息是一个form
      dialogFormVisible: false,
      isEdit: false, //是否修改
      editId: "",
      delId: "",
      show3: false,
      choiceMap: { 身份证: 0, 护照: 1, 男: 0, 女: 1 },
      //direction: 'rtl',
      form: {
        id: "", //学号
        person_name: "",
        gender: "",
        person_id_type: "",
        person_id: "", //身份证号
        country: "",
        birth: "",
        class_id: "",
        class_name: "",
        major_id: "",
        major_name: "",
        family_address: "",
        family_zipcode: "",
        family_tel: "",
        enroll_date: "",
        email: ""
      },

      //两套rule体系
      searchRules: {
        name: [
          { min: 2, max: 10, message: "长度在 2 到 10 个字符", trigger: "blur" }
        ]
      },

      rules: {
        id: [{ required: true, message: "必填", trigger: "blur" }],
        person_name: [
          { required: true, message: "必填", trigger: "blur" },
          { min: 2, max: 5, message: "长度在 2 到 5 个字符", trigger: "blur" }
        ],
        person_id_type: [{ required: true, message: "必填", trigger: "blur" }],
        person_id: [{ required: true, message: "必填", trigger: "blur" }]
        // moblie: [
        //   { type: 'number', message: '年龄必须为数字值'}
        // ]
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
      if (opt["person_id_type"]) {
        opt["person_id_type"] = this.choiceMap[opt["person_id_type"]];
      }
      if (opt["gender"]) {
        opt["gender"] = this.choiceMap[opt["gender"]];
      }
      this.$http
        .get(url, opt)
        .then(function(res) {
          if (url === "http://127.0.0.1:8000/api/student/del") {
            console.log(_this.tableData);
            _this.tableData.splice(_this.delIndex, 1);
          } else if (url === "http://127.0.0.1:8000/api/student/get") {
            console.log(res);
            _this.tableData = res.data["list"];
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    sendPostRequest(url, opt = {}) {
      var _this = this;
      if (opt["person_id_type"]) {
        opt["person_id_type"] = this.choiceMap[opt["person_id_type"]];
      }
      if (opt["gender"]) {
        opt["gender"] = this.choiceMap[opt["gender"]];
      }
      console.log(opt);
      this.$http
        .post(url, JSON.stringify(opt), { emulateJSON: true })
        .then(function(res) {
          console.log(res);
          var resbody = JSON.parse(res.bodyText);

          if (url === "http://127.0.0.1:8000/api/student/add") {
            if (resbody["code"] == 0) {
              _this.$message.error("添加学生失败：" + resbody["msg"]);
            } else {
              _this.getAllData();
            }
          } else if (url === "http://127.0.0.1:8000/api/student/mod") {
            if (resbody["code"] == 0) {
              _this.$message.error("修改学生信息失败：" + resbody["msg"]);
            } else {
              _this.$http
                .get("http://127.0.0.1:8000/api/student/get", {
                  params: { id: _this.editId }
                })
                .then(function(res) {
                  console.log(res);
                  _this.tableData[_this.editIndex] = res.data["list"][0];
                });
            }
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
            let subForm = that.form;
            delete subForm.id;
            let opt = {
              where: {
                id: that.editId
              },
              update: subForm
            };
            // 修改
            that.sendPostRequest("http://127.0.0.1:8000/api/student/mod", opt);
          } else {
            // 新增
            that.sendPostRequest(
              "http://127.0.0.1:8000/api/student/add",
              that.simplify(that.form)
            );
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
        .get("http://127.0.0.1:8000/api/student/get")
        .then(function(res) {
          var resbody = JSON.parse(res.bodyText);
          if (resbody["code"] == 0) {
            _this.$message.error("查询学生失败");
          } else {
            _this.tableData = res.data["list"];
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
      this.form.person_name = selfData.person_name;
      this.form.gender = selfData.gender;
      this.form.person_id_type = selfData.person_id_type;
      this.form.person_id = selfData.person_id;
      this.form.country = selfData.country;
      this.form.birth = selfData.birth;
      this.form.class_id = selfData.class_id;
      this.form.class_name = selfData.class_name;
      this.form.major_id = selfData.major_id;
      this.form.major_name = selfData.major_name;
      this.form.family_address = selfData.family_address;
      this.form.family_zipcode = selfData.family_zipcode;
      this.form.family_tel = selfData.family_tel;
      this.form.enroll_date = selfData.enroll_date;
      this.form.email = selfData.email;
    },

    openDialog(index) {
      this.delId = this.tableData[index]["id"];
      this.delIndex = index;
      this.dialogVisible = true;
    },

    delData() {
      var _this = this;
      _this.dialogVisible = false;
      this.sendGetRequest("http://127.0.0.1:8000/api/student/del", {
        params: { id: this.delId }
      });
    },

    mysearchData() {
      console.log(this.simplify(this.form));
      this.sendGetRequest("http://127.0.0.1:8000/api/student/get", {
        params: this.simplify(this.form)
      });
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

