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
              label="专业代码"
              prop="id"
              style="width: 20%; left: 30px; position: absolute;"
            >
              <el-input v-model="form.id"></el-input>
            </el-form-item>
            <el-form-item label="专业名称" prop="name" style="width: 20%">
              <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="专业地址" prop="address" style="width: 20%">
              <el-input v-model="form.address"></el-input>
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
              label="专业负责人"
              prop="charge_person_id"
              style="width: 20%; position: relative;"
            >
              <el-input v-model="form.charge_person"></el-input>
            </el-form-item>
            <el-form-item label="所属校区" prop="campus_id" style="width: 20%">
              <el-input v-model="form.campus_id"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-collapse-transition>

      <!--/div-->
    </el-row>
    <el-scrollbar>
      <el-table :data="tableData" stripe style="width: 100%">
        <el-table-column prop="id" label="专业代码" align="center"></el-table-column>
        <el-table-column prop="name" label="专业名称" align="center"></el-table-column>
        <el-table-column prop="address" label="专业地址" align="center"></el-table-column>
        <el-table-column prop="charge_person_id" label="专业负责人工号" align="center"></el-table-column>
        <el-table-column prop="charge_person_name" label="专业负责人" align="center"></el-table-column>
        <el-table-column prop="campus_id" label="所属校区代码" align="center"></el-table-column>
        <el-table-column prop="campus_name" label="所属校区名称" align="center"></el-table-column>

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
        <el-form-item label="专业代码" prop="id">
          <el-input v-model="form.id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="专业名称" prop="name">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="专业地址" prop="address">
          <el-input v-model="form.address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="专业负责人工号" prop="charge_person_id">
          <el-input v-model="form.charge_person_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="所属校区代码" prop="campus_id">
          <el-input v-model="form.campus_id" autocomplete="off"></el-input>
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
        id: "",
        name: "",
        address: "",
        charge_person_id: "",
        campus_id: "",
        campus_name: "",
        charge_person_name: ""
      },

      //两套rule体系
      searchRules: {},

      rules: {
        id: [{ required: true, message: "必填", trigger: "blur" }],
        name: [{ required: true, message: "必填", trigger: "blur" }],
        address: [{ required: true, message: "必填", trigger: "blur" }],
        charge_person_id: [{ message: "必填", trigger: "blur" }],
        campus_id: [{ required: true, message: "必填", trigger: "blur" }]
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
        if (obj[key] && key !== "campus_name" && key !== "charge_person_name")
          newobj[key] = obj[key];
      }
      return newobj;
    },

    sendGetRequest(url, opt = {}) {
      var _this = this;
      this.$http
        .get(url, opt)
        .then(function(res) {
          if (url === "http://127.0.0.1:8000/api/major/del") {
            console.log(_this.tableData);
            _this.tableData.splice(_this.delIndex, 1);
          } else if (url === "http://127.0.0.1:8000/api/major/get") {
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
          if (url === "http://127.0.0.1:8000/api/major/add") {
            if (resbody["code"] == 0) {
              _this.$message.error("添加专业失败：" + resbody["msg"]);
            } else {
              _this.getAllData();
            }
          } else if (url === "http://127.0.0.1:8000/api/major/mod") {
            console.log(res);
            if (resbody["code"] == 0) {
              _this.$message.error("修改专业失败：" + resbody["msg"]);
            } else {
              //考虑改为get请求
              _this.$http
                .get("http://127.0.0.1:8000/api/major/get", {
                  params: { id: _this.editId }
                })
                .then(function(res) {
                  console.log(res);
                  _this.tableData[_this.editIndex] = res.data["list"][0];
                });
              // for (let key in opt.update)
              //   _this.tableData[_this.editIndex][key] = opt.update[key];
              // this.reload();
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
            delete subForm.campus_name;
            delete subForm.charge_person_name;
            let opt = {
              where: {
                id: that.editId
              },
              update: subForm
            };
            // 修改
            that.sendPostRequest("http://127.0.0.1:8000/api/major/mod", opt);
          } else {
            // 新增
            that.sendPostRequest(
              "http://127.0.0.1:8000/api/major/add",
              this.simplify(that.form)
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
        .get("http://127.0.0.1:8000/api/major/get")
        .then(function(res) {
          var resbody = JSON.parse(res.bodyText);
          if (resbody["code"] == 0) {
            _this.$message.error("查询专业失败");
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
      this.form.address = selfData.address;
      this.form.charge_person_id = selfData.charge_person_id;
      this.form.campus_id = selfData.campus_id;
    },

    openDialog(index) {
      this.delId = this.tableData[index]["id"];
      this.delIndex = index;
      this.dialogVisible = true;
    },

    delData() {
      var _this = this;
      _this.dialogVisible = false;
      this.sendGetRequest("http://127.0.0.1:8000/api/major/del", {
        params: { id: this.delId }
      });
    },

    mysearchData() {
      console.log(this.simplify(this.form));
      this.sendGetRequest("http://127.0.0.1:8000/api/major/get", {
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

