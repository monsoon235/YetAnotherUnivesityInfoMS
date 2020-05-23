<template>
  <div class="index">
    <!-- <div style='height: 60px'> 
      <span class='font'>欢迎进入本校学生信息管理模块</span>
      <p class='text'>学生是挚友，是学校引以为傲的资本，管理学生信息非常重要哦</p>
    </div>-->
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
              label="课堂号"
              prop="lecture_id"
              style="width: 20%; left: 30px; position: absolute;"
            >
              <el-input v-model="form.lecture_id"></el-input>
            </el-form-item>
            <el-form-item label="学号" prop="student_id" style="width: 20%">
              <el-input v-model="form.student_id"></el-input>
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
              label="选课日期"
              prop="year"
              style="width: 20%; left: 30px; position: absolute;"
            >
              <el-input v-model="form.year"></el-input>
            </el-form-item>
            <el-form-item label="选课学期" prop="term">
              <el-select v-model="form.term" placeholder="请选择学期">
                <el-option label="春" value="0" autocomplete="off"></el-option>
                <el-option label="秋" value="1" autocomplete="off"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="考试成绩" prop="score" style="width: 20%">
              <el-input v-model="form.score"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-collapse-transition>

      <!--/div-->
    </el-row>
    <el-scrollbar>
      <el-table :data="tableData" stripe style="width: 100%">
        <el-table-column prop="id" label="序号" align="center"></el-table-column>
        <el-table-column prop="lecture_id" label="课堂号" align="center"></el-table-column>
        <el-table-column prop="course_name" label="课程名称" align="center"></el-table-column>
        <el-table-column prop="teacher_name" label="授课教师" align="center"></el-table-column>
        <el-table-column prop="student_id" label="学号" align="center"></el-table-column>
        <el-table-column prop="student_name" label="学生姓名" align="center"></el-table-column>
        <el-table-column prop="year" label="选课日期" align="center"></el-table-column>
        <el-table-column label="选课学期" align="center">
          <template slot-scope="scope">
            <i v-if="scope.row.term===0">春</i>
            <i v-else>秋</i>
          </template>
        </el-table-column>
        <el-table-column prop="score" label="考试成绩" align="center" sortable></el-table-column>

        <el-table-column label="操作" align="center">
          <template slot-scope="scope">
            <el-button type="primary" @click="editData(scope.$index)">修改</el-button>
            <el-button type="danger" @click="openDialog(scope.$index)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-scrollbar>

    <el-dialog title="填写你的信息" :visible.sync="dialogFormVisible" style="height: 100%">
      <el-form :model="form" :rules="rules" ref="form">
        <el-form-item label="课程号" prop="lecture_id">
          <el-input v-model="form.lecture_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="学号" prop="student_id">
          <el-input v-model="form.student_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="选课日期" prop="year">
          <el-input v-model="form.year" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="选课学期" prop="term">
          <el-select v-model="form.term" placeholder="请选择学期">
            <el-option label="春" value="0" autocomplete="off"></el-option>
            <el-option label="秋" value="1" autocomplete="off"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="考试成绩" prop="score">
          <el-input v-model="form.score" autocomplete="off"></el-input>
        </el-form-item>
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
      //direction: 'rtl',
      form: {
        lecture_id: "",
        student_id: "",
        year: "",
        term: "",
        score: null,
        course_name: "",
        teacher_name: "",
        student_name: ""
      },

      //两套rule体系
      searchRules: {
        score: [
          { type: "number", message: "成绩必须为数字值", trigger: "blur" }
        ]
      },

      rules: {
        lecture_id: [{ required: true, message: "必填", trigger: "blur" }],
        student_id: [{ required: true, message: "必填", trigger: "blur" }],
        year: [{ required: true, message: "必填", trigger: "blur" }],
        term: [{ required: true, message: "必填", trigger: "blur" }],
        score: [
          { type: "number", message: "成绩必须为数字值", trigger: "blur" }
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
        if (
          obj[key] &&
          key !== "course_name" &&
          key !== "teacher_name" &&
          key !== "student_name"
        )
          newobj[key] = obj[key];
      }
      return newobj;
    },

    sendGetRequest(url, opt = {}) {
      var _this = this;
      this.$http
        .get(url, opt)
        .then(function(res) {
          if (url === "http://127.0.0.1:8000/api/selection/del") {
            console.log(_this.tableData);
            _this.tableData.splice(_this.delIndex, 1);
          } else if (url === "http://127.0.0.1:8000/api/selection/get") {
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

          if (url === "http://127.0.0.1:8000/api/selection/add") {
            if (resbody["code"] == 0) {
              _this.$message.error("添加选课失败：" + resbody["msg"]);
            } else {
              _this.getAllData();
            }
          } else if (url === "http://127.0.0.1:8000/api/selection/mod") {
            if (resbody["code"] == 0) {
              _this.$message.error("修改选课信息失败：" + resbody["msg"]);
            } else {
              _this.$http
                .get("http://127.0.0.1:8000/api/selection/get", {
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
            delete subForm.course_name;
            delete subForm.teacher_name;
            delete subForm.student_name;
            let opt = {
              where: {
                id: that.editId
              },
              update: subForm
            };
            // 修改
            that.sendPostRequest(
              "http://127.0.0.1:8000/api/selection/mod",
              opt
            );
          } else {
            // 新增
            that.sendPostRequest(
              "http://127.0.0.1:8000/api/selection/add",
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
        .get("http://127.0.0.1:8000/api/selection/get")
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
      this.form.lecture_id = selfData.lecture_id;
      this.form.student_id = selfData.student_id;
      this.form.year = selfData.year;
      this.form.term = selfData.term;
      this.form.score = selfData.score;
    },

    openDialog(index) {
      this.delId = this.tableData[index]["id"];
      this.delIndex = index;
      this.dialogVisible = true;
    },

    delData() {
      var _this = this;
      _this.dialogVisible = false;
      this.sendGetRequest("http://127.0.0.1:8000/api/selection/del", {
        params: { id: this.delId }
      });
    },

    mysearchData() {
      console.log(this.simplify(this.form));
      this.sendGetRequest("http://127.0.0.1:8000/api/selection/get", {
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

