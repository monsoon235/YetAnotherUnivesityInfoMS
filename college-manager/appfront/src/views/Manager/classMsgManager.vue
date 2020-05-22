<template>
  <div>
    <!-- <div style="height: 90px">
      <span class='font'>欢迎进入本校班级管理模块</span>
      <p class='text'>尊敬的管理员您好，班级的存在与设置记录了学校的成长，您只可以进行查询、增加、修改，请谨慎操作(如勿操作，请联系后台管理员)</p>
    </div>-->
    <div>
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
          <div v-if="show3">
            <br />
            <el-form
              :inline="true"
              :model="form"
              :rules="searchRules"
              ref="form"
              label-width="100px"
              class="demo-ruleForm"
            >
              <el-form-item
                label="班级编号"
                prop="id"
                style="width: 20%; left: 30px; position: absolute;"
              >
                <el-input v-model="form.id"></el-input>
              </el-form-item>
              <el-form-item label="班级名称" prop="name" style="width: 20%">
                <el-input v-model="form.name"></el-input>
              </el-form-item>
              <el-form-item label="建班年月" prop="date" style="width: 20%">
                <el-input v-model="form.found_date"></el-input>
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
              <el-form-item label="所属年级" prop="grade" style="width: 20%">
                <el-input v-model="form.grade"></el-input>
              </el-form-item>
              <el-form-item label="所属专业" prop="major_id" style="position: relative;">
                <el-input v-model="form.major_id"></el-input>
              </el-form-item>
              <el-form-item label="班主任工号" prop="charge_teacher_id" style="width: 20%">
                <el-input v-model="form.charge_teacher_id"></el-input>
              </el-form-item>
            </el-form>
          </div>
        </el-collapse-transition>
      </el-row>

      <el-table :data="tableData" stripe style="width: 100%">
        <!-- <el-table-column
	        prop="className"
	        label="班级名">
        </el-table-column>-->
        <!-- <el-table-column
	        prop="stage"
	        label="适应阶段">
        </el-table-column>-->
        <el-table-column prop="id" label="班级编号"></el-table-column>
        <el-table-column prop="name" label="班级名"></el-table-column>
        <el-table-column prop="found_date" label="建班年月"></el-table-column>
        <el-table-column prop="grade" label="所属年级"></el-table-column>
        <el-table-column prop="major_id" label="所属专业代码"></el-table-column>
        <el-table-column prop="major_name" label="所属专业"></el-table-column>
        <el-table-column prop="charge_teacher_id" label="班主任工号"></el-table-column>
        <el-table-column prop="charge_teacher_name" label="班主任"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" @click="editData(scope.$index)">修改</el-button>
            <el-button type="danger" @click="openDialog(scope.$index)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <div style="margin-top: -60px">
        <el-dialog title="请填写班级信息" :visible.sync="dialogFormVisible" style="height: 100%；">
          <el-form :model="form" :rules="rules" ref="form">
            <el-form-item label="班级编号" prop="id">
              <el-input v-model="form.id" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="班级名" prop="name">
              <el-input v-model="form.name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="建班年月" prop="found_date">
              <el-input v-model="form.found_date" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="所属年级" prop="grade">
              <el-input v-model="form.grade" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="所属专业代码" prop="major_id">
              <el-input v-model="form.major_id" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="班主任工号" prop="charge_teacher_id">
              <el-input v-model="form.charge_teacher_id" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="submitFrom">确 定</el-button>
          </div>
        </el-dialog>
      </div>

      <el-dialog title="提示" :visible.sync="dialogVisible" width="30%">
        <span>确定要删除信息</span>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="delData">确 定</el-button>
        </span>
      </el-dialog>
    </div>
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
      show3: false,
      form: {
        id: "",
        name: "",
        found_date: "",
        grade: "",
        major_id: "",
        charge_teacher_id: "",
        major_name: "",
        charge_teacher_name: ""
      },
      rules: {
        id: [{ required: true, message: "请填写班级代码", trigger: "blur" }],
        name: [{ required: true, message: "请填写班级名称", trigger: "blur" }],
        found_date: [
          { required: true, message: "请正确填写建班年月", trigger: "blur" }
        ],
        grade: [{ required: true, message: "请填写所属年级", trigger: "blur" }],
        major_id: [
          { required: true, message: "请填写所属专业", trigger: "blur" }
        ],
        charge_teacher_id: [
          { required: true, message: "请填写班主任工号", trigger: "blur" }
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
        if (obj[key] && key !== "major_name" && key !== "charge_teacher_name")
          newobj[key] = obj[key];
      }
      return newobj;
    },

    sendGetRequest(url, opt = {}) {
      var _this = this;
      this.$http
        .get(url, opt)
        .then(function(res) {
          if (url === "http://127.0.0.1:8000/api/class/del") {
            console.log(_this.tableData);
            _this.tableData.splice(_this.delIndex, 1);
          } else if (url === "http://127.0.0.1:8000/api/class/get") {
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
      console.log(opt);
      this.$http
        .post(url, JSON.stringify(opt), { emulateJSON: true })
        .then(function(res) {
          console.log(res);
          var resbody = JSON.parse(res.bodyText);
          if (url === "http://127.0.0.1:8000/api/class/add") {
            if (resbody["code"] == 0) {
              _this.$message.error("修改学生信息失败: " + resbody["msg"]);
            }else{
            _this.getAllData();
            }
          } else if (url === "http://127.0.0.1:8000/api/class/mod") {
            if (resbody["code"] == 0) {
              _this.$message.error("修改学生信息失败: " + resbody["msg"]);
            } else {
              _this.$http
                .get("http://127.0.0.1:8000/api/class/get", {
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
            delete subForm.lecture;
            delete subForm.student;
            delete subForm.major_name;
            delete subForm.charge_teacher_name;
            let opt = {
              where: {
                id: that.editId
              },
              update: subForm
            };
            // 修改
            that.sendPostRequest("http://127.0.0.1:8000/api/class/mod", opt);
          } else {
            // 新增
            that.sendPostRequest(
              "http://127.0.0.1:8000/api/class/add",
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
        .get("http://127.0.0.1:8000/api/class/get")
        .then(function(res) {
          var resbody = JSON.parse(res.bodyText);
          if (resbody["code"] == 0) {
            _this.$message.error("查询选课失败");
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
      this.form.name = selfData.name;
      this.form.found_date = selfData.found_date;
      this.form.grade = selfData.grade;
      this.form.major_id = selfData.major_id;
      this.form.charge_teacher_id = selfData.charge_teacher_id;
    },

    openDialog(index) {
      (this.delId = this.tableData[index]["id"]), (this.delIndex = index);
      this.dialogVisible = true;
    },

    delData() {
      var _this = this;
      _this.dialogVisible = false;
      this.sendGetRequest("http://127.0.0.1:8000/api/class/del", {
        params: { id: this.delId }
      });
    },

    mysearchData() {
      console.log(this.simplify(this.form));
      this.sendGetRequest("http://127.0.0.1:8000/api/class/get", {
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