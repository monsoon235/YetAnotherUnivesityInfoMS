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
            <el-row type="flex" class="row-bg">
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="异动编号" prop="id">
                    <el-input v-model="form.id" :disabled="isEdit"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="学号" prop="student_id">
                    <el-input v-model="form.student_id"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="原班级代码" prop="from_class_id">
                    <el-input v-model="form.from_class_id"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="现班级代码" prop="to_class_id">
                    <el-input v-model="form.to_class_id"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <el-button type="warning" plain @click="mysearchData">搜索</el-button>
              </el-col>
            </el-row>

            <el-row type="flex" class="row-bg">
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="异动类型" prop="type">
                    <el-select v-model="form.type" placeholder="请选择类型">
                      <el-option label="转专业" value="0" autocomplete="off"></el-option>
                      <el-option label="降级" value="1" autocomplete="off"></el-option>
                    </el-select>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="转出团关系" v-if="form.type==0" prop="extra">
                    <el-select v-model="form.extra">
                      <el-option label="是" value="0" autocomplete="off"></el-option>
                      <el-option label="否" value="1" autocomplete="off"></el-option>
                      <el-option label="不是团员" value="2" autocomplete="off"></el-option>
                    </el-select>
                  </el-form-item>
                  <el-form-item label="降级原因" v-if="form.type==1" prop="extra">
                    <el-select v-model="form.extra">
                      <el-option label="休学" value="0" autocomplete="off"></el-option>
                      <el-option label="支教" value="1" autocomplete="off"></el-option>
                    </el-select>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="异动日期" prop="date">
                    <el-input v-model="form.date"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content"></div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content"></div>
              </el-col>
            </el-row>
          </el-form>
        </div>
      </el-collapse-transition>

      <!--/div-->
    </el-row>
    <el-scrollbar>
      <el-table :data="tableData" stripe style="width: 100%">
        <el-table-column prop="id" label="异动编号" align="center"></el-table-column>
        <el-table-column prop="student_id" label="学号" align="center"></el-table-column>
        <el-table-column label="异动类型" align="center">
          <template slot-scope="scope">
            <i v-if="scope.row.type===0">转专业</i>
            <i v-else>降级</i>
          </template>
        </el-table-column>
        <el-table-column label="是否转出团关系" align="center">
          <template slot-scope="scope">
            <i v-if="scope.row.type===1">\</i>
            <i v-else-if="scope.row.extra===0">是</i>
            <i v-else-if="scope.row.extra===1">否</i>
            <i v-else>不是团员</i>
          </template>
        </el-table-column>
        <el-table-column label="降级原因" align="center">
          <template slot-scope="scope">
            <i v-if="scope.row.type===0">\</i>
            <i v-else-if="scope.row.extra===0">休学</i>
            <i v-else>支教</i>
          </template>
        </el-table-column>
        <el-table-column prop="from_class_id" label="原班级代码" align="center"></el-table-column>
        <el-table-column prop="to_class_id" label="现班级代码" align="center"></el-table-column>
        <el-table-column prop="date" label="异动日期" align="center"></el-table-column>

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
        <el-form-item label="异动编号" prop="id">
          <el-input v-model="form.id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="异动类型" prop="type">
          <el-select v-model="form.type" placeholder="请选择类型">
            <el-option label="转专业" value="0" autocomplete="off"></el-option>
            <el-option label="降级" value="1" autocomplete="off"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="转出团关系" v-if="form.type==0" prop="extra">
          <el-select v-model="form.extra" placeholder="是否转出">
            <el-option label="是" value="0" autocomplete="off"></el-option>
            <el-option label="否" value="1" autocomplete="off"></el-option>
            <el-option label="不是团员" value="2" autocomplete="off"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="降级原因" v-if="form.type==1" prop="extra">
          <el-select v-model="form.extra" placeholder="请选择">
            <el-option label="休学" value="0" autocomplete="off"></el-option>
            <el-option label="支教" value="1" autocomplete="off"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="原班级代码" prop="from_class_id">
          <el-input v-model="form.from_class_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="现班级代码" prop="to_class_id">
          <el-input v-model="form.to_class_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="异动日期" prop="date">
          <el-input v-model="form.date" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="学号" prop="student_id">
          <el-input v-model="form.student_id" autocomplete="off"></el-input>
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
        from_class_id: "",
        to_class_id: "",
        type: null,
        date: "",
        student_id: "",
        extra: null
      },

      //两套rule体系
      searchRules: {
        date: [{ max: 7, message: "XXXX-YY", trigger: "blur" }]
      },

      rules: {
        id: [{ required: true, message: "必填", trigger: "blur" }],
        student_id: [{ required: true, message: "必填", trigger: "blur" }],
        type: [{ required: true, message: "必填", trigger: "blur" }]
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
          if (url === "/api/adjustment/del") {
            console.log(_this.tableData);
            _this.tableData.splice(_this.delIndex, 1);
          } else if (url === "/api/adjustment/get") {
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
          if (url === "/api/adjustment/add") {
            if (resbody["code"] == 0) {
              _this.$message.error("添加学籍异动失败: " + resbody["msg"]);
            } else {
              _this.getAllData();
            }
          } else if (url === "/api/adjustment/mod") {
            if (resbody["code"] == 0) {
              _this.$message.error("修改学籍异动信息失败: " + resbody["msg"]);
            } else {
              _this.$http
                .get("/api/adjustment/get", {
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
            that.sendPostRequest("/api/adjustment/mod", opt);
          } else {
            // 新增
            that.sendPostRequest("/api/adjustment/add", that.form);
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
        .get("/api/adjustment/get")
        .then(function(res) {
          var resbody = JSON.parse(res.bodyText);
          console.log(res);
          if (resbody["code"] == 0) {
            _this.$message.error("查询学籍异动失败");
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
      this.form.from_class_id = selfData.from_class_id;
      this.form.to_class_id = selfData.to_class;
      this.form.type = selfData.type;
      this.form.date = selfData.date;
      this.form.student_id = selfData.student_id;
      this.form.extra = selfData.extra;
    },

    openDialog(index) {
      this.delId = this.tableData[index]["id"];
      this.delIndex = index;
      this.dialogVisible = true;
    },

    delData() {
      var _this = this;
      _this.dialogVisible = false;
      this.sendGetRequest("/api/adjustment/del", {
        params: { id: this.delId }
      });
    },

    mysearchData() {
      console.log(this.simplify(this.form));
      this.sendGetRequest("/api/adjustment/get", {
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

