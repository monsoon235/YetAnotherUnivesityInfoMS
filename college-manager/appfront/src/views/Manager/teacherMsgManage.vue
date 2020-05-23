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
                  <el-form-item label="姓名" prop="name">
                    <el-input v-model="form.name"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="工号" prop="id">
                    <el-input v-model="form.id"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="出生日期" prop="birth">
                    <el-date-picker type="date" placeholder="选择日期" v-model="form.birth"></el-date-picker>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="性别" prop="gender">
                    <el-radio-group v-model="form.gender">
                      <el-radio label="男"></el-radio>
                      <el-radio label="女"></el-radio>
                    </el-radio-group>
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
                  <el-form-item label="职称" prop="titles">
                    <el-select v-model="form.titles" multiple placeholder="请选择职称">
                      <el-option label="教授" value="教授" autocomplete="off"></el-option>
                      <el-option label="副教授" value="副教授" autocomplete="off"></el-option>
                    </el-select>
                  </el-form-item>
                </div>
              </el-col>

              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="专业代码" prop="major_id">
                    <el-input v-model="form.major_id"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="专业名称" prop="major_name">
                    <el-input v-model="form.major_name"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="入职时间" prop="enroll_date">
                    <el-date-picker type="date" placeholder="选择日期" v-model="form.enroll_date"></el-date-picker>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple"></div>
              </el-col>
            </el-row>

            <el-row type="flex" class="row-bg">
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="身份证类型" prop="person_id_type">
                    <el-radio-group v-model="form.person_id_type">
                      <el-radio label="身份证"></el-radio>
                      <el-radio label="护照"></el-radio>
                    </el-radio-group>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="身份证号" prop="person_id">
                    <el-input v-model="form.person_id"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="国籍" prop="country">
                    <el-input v-model="form.country"></el-input>
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

            <el-row type="flex" class="row-bg">
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="家庭住址" prop="family_address">
                    <el-input v-model="form.family_address"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="联系电话" prop="family_tel">
                    <el-input v-model="form.family_tel"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="邮编" prop="family_zipcode">
                    <el-input v-model="form.family_zipcode"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple-light">
                  <el-form-item label="电子邮箱" prop="email">
                    <el-input v-model="form.email"></el-input>
                  </el-form-item>
                </div>
              </el-col>
              <el-col :span="6">
                <div class="grid-content bg-purple"></div>
              </el-col>
            </el-row>
          </el-form>
        </div>
      </el-collapse-transition>

      <!--/div-->
    </el-row>
    <el-row>
      <el-checkbox-group v-model="checkList">
        <el-checkbox label="工号"></el-checkbox>
        <el-checkbox label="姓名"></el-checkbox>
        <el-checkbox label="性别"></el-checkbox>
        <el-checkbox label="职称"></el-checkbox>
        <el-checkbox label="身份证类型"></el-checkbox>
        <el-checkbox label="身份证号"></el-checkbox>

        <el-checkbox label="国籍"></el-checkbox>

        <el-checkbox label="出生日期"></el-checkbox>
        <el-checkbox label="专业代码"></el-checkbox>
        <el-checkbox label="专业名称"></el-checkbox>
        <el-checkbox label="家庭住址"></el-checkbox>
        <el-checkbox label="联系电话"></el-checkbox>
        <el-checkbox label="入职时间"></el-checkbox>
        <el-checkbox label="电子邮箱"></el-checkbox>
      </el-checkbox-group>
    </el-row>
    <el-scrollbar>
      <el-table :data="tableData" stripe style="width: 100%">
        <el-table-column prop="id" label="工号" align="center" v-if="checkList.includes('工号')"></el-table-column>
        <el-table-column
          prop="person_name"
          label="姓名"
          align="center"
          v-if="checkList.includes('姓名')"
        ></el-table-column>
        <el-table-column label="性别" align="center" v-if="checkList.includes('性别')">
          <template slot-scope="scope">
            <i v-if="scope.row.gender===0">男</i>
            <i v-else>女</i>
          </template>
        </el-table-column>
        <el-table-column label="职称" align="center" v-if="checkList.includes('职称')">
          <template slot-scope="scope">
            <i v-if="scope.row.title===0">教授</i>
            <i v-else>副教授</i>
          </template>
        </el-table-column>
        <el-table-column
          prop="birth"
          label="出生日期"
          width="220"
          align="center"
          v-if="checkList.includes('出生日期')"
        ></el-table-column>
        <el-table-column
          prop="major_id"
          label="专业代码"
          align="center"
          v-if="checkList.includes('专业代码')"
        ></el-table-column>
        <el-table-column
          prop="major_name"
          label="专业名称"
          align="center"
          v-if="checkList.includes('专业名称')"
        ></el-table-column>
        <el-table-column
          label="身份证类型"
          width="150"
          align="center"
          v-if="checkList.includes('身份证类型')"
        >
          <template slot-scope="scope">
            <i v-if="scope.row.person_id_type===0">身份证</i>
            <i v-else>护照</i>
          </template>
        </el-table-column>
        <el-table-column
          prop="person_id"
          label="身份证号"
          width="220"
          align="center"
          v-if="checkList.includes('身份证号')"
        ></el-table-column>
        <el-table-column prop="country" label="国籍" align="center" v-if="checkList.includes('国籍')"></el-table-column>
        <el-table-column
          prop="enroll_date"
          label="入职时间"
          width="220"
          align="center"
          v-if="checkList.includes('入职时间')"
        ></el-table-column>
        <el-table-column
          prop="family_address"
          label="家庭住址"
          width="220"
          align="center"
          v-if="checkList.includes('家庭住址')"
        ></el-table-column>
        <el-table-column
          prop="family_zipcode"
          label="邮编"
          align="center"
          v-if="checkList.includes('邮编')"
        ></el-table-column>
        <el-table-column
          prop="family_tel"
          label="联系电话"
          align="center"
          v-if="checkList.includes('联系电话')"
        ></el-table-column>
        <el-table-column
          prop="email"
          width="220"
          label="电子邮箱"
          align="center"
          v-if="checkList.includes('电子邮箱')"
        ></el-table-column>
        <el-table-column label="操作" width="220" align="center">
          <template slot-scope="scope">
            <el-button type="primary" @click="editData(scope.$index)">修改</el-button>
            <el-button type="danger" @click="openDialog(scope.$index)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-scrollbar>

    <el-dialog title="填写你的信息" :visible.sync="dialogFormVisible" style="height: 100%">
      <el-form :model="form" :rules="rules" ref="form" label-width="100px">
        <el-form-item label="工号" prop="id" autocomplete="off">
          <el-input v-model="form.id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="person_name">
          <el-input v-model="form.person_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="gender">
          <el-select v-model="form.gender" placeholder="请选择性别" style="margin-left: -280px;">
            <el-option label="男" value="男" autocomplete="off"></el-option>
            <el-option label="女" value="女" autocomplete="off"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="职称" prop="title">
          <el-select v-model="form.title" placeholder="请选择职称" style="margin-left: -280px;">
            <el-option label="教授" value="教授" autocomplete="off"></el-option>
            <el-option label="副教授" value="副教授" autocomplete="off"></el-option>
          </el-select>
        </el-form-item>
        <!-- <el-form-item label="性别">
          <el-input v-model="form.sex" autocomplete="off"></el-input>
        </el-form-item>-->
        <el-form-item label="出生日期" prop="birth">
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.birth"></el-date-picker>
          </el-col>
        </el-form-item>

        <el-form-item label="专业代码" prop="major_id">
          <el-input v-model="form.major_id"></el-input>
        </el-form-item>

        <el-form-item label="专业名称" prop="major_name">
          <el-input v-model="form.major_name"></el-input>
        </el-form-item>

        <el-form-item label="身份证类型" prop="person_id_type">
          <el-radio-group v-model="form.person_id_type" style="margin-left: -280px;">
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

        <el-form-item label="入职时间" prop="enroll_date">
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.enroll_date"></el-date-picker>
          </el-col>
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
        <el-form-item label="登录密码" prop="password">
          <el-input v-model="form.password" :disabled="isEdit"></el-input>
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
      checkList: [
        "工号",
        "姓名",
        "性别",
        "职称",
        "身份证类型",
        "身份证号",
        "国籍",
        "出生日期",
        "专业代码",
        "专业名称",
        "家庭住址",
        "联系电话",
        "入职时间",
        "电子邮箱"
      ],
      choiceMap: { 身份证: 0, 护照: 1, 男: 0, 女: 1, 教授: 0, 副教授: 1 },
      //direction: 'rtl',
      form: {
        id: "", //工号
        person_name: "",
        gender: "",
        title: "",
        titles: [],
        person_id_type: "",
        person_id: "", //身份证号
        country: "",
        birth: "",
        major_id: "",
        major_name: "",
        family_address: "",
        family_zipcode: "",
        family_tel: "",
        enroll_date: "",
        email: "",
        password: ""
      },

      //两套rule体系
      searchRules: {
        name: [
          { min: 2, max: 5, message: "长度在 2 到 8 个字符", trigger: "blur" }
        ]
      },

      rules: {
        person_name: [
          { required: true, message: "必填", trigger: "blur" },
          { min: 2, max: 5, message: "长度在 2 到 8 个字符", trigger: "blur" }
        ],
        person_id: [{ required: true, message: "必填", trigger: "blur" }],
        id: [{ required: true, message: "必填", trigger: "blur" }]
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
      if (newobj["person_id_type"]) {
        newobj["person_id_type"] = this.choiceMap[newobj["person_id_type"]];
      }
      if (newobj["gender"]) {
        newobj["gender"] = this.choiceMap[newobj["gender"]];
      }
      if (newobj["title"]) {
        newobj["title"] = this.choiceMap[newobj["title"]];
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
      if (opt["title"]) {
        opt["title"] = this.choiceMap[opt["title"]];
      }
      this.$http
        .get(url, opt)
        .then(function(res) {
          if (url === "/api/teacher/del") {
            console.log(_this.tableData);
            _this.tableData.splice(_this.delIndex, 1);
          } else if (url === "/api/teacher/get") {
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
      if (opt.update) {
        if (opt["update"]["person_id_type"]) {
          opt["update"]["person_id_type"] = this.choiceMap[
            opt["update"]["person_id_type"]
          ];
        }
        if (opt["update"]["gender"]) {
          opt["update"]["gender"] = this.choiceMap[opt["update"]["gender"]];
        }
        if (opt["update"]["title"]) {
          opt["update"]["title"] = this.choiceMap[opt["update"]["title"]];
        }
      } else {
        if (opt["person_id_type"]) {
          opt["person_id_type"] = this.choiceMap[opt["person_id_type"]];
        }
        if (opt["gender"]) {
          opt["gender"] = this.choiceMap[opt["gender"]];
        }
        if (opt["title"]) {
          opt["title"] = this.choiceMap[opt["title"]];
        }
      }
      this.$http
        .post(url, JSON.stringify(opt), { emulateJSON: true })
        .then(function(res) {
          console.log(res);
          var resbody = JSON.parse(res.bodyText);
          // 将数据存储起来
          if (url === "/api/teacher/add") {
            if (resbody["code"] == 0) {
              _this.$message.error("添加教师失败：" + resbody["msg"]);
            } else {
              _this.getAllData();
            }
          } else if (url === "/api/teacher/mod") {
            if (resbody["code"] == 0) {
              _this.$message.error("修改教师信息失败：" + resbody["msg"]);
            } else {
              _this.$http
                .get("/api/teacher/get", {
                  params: { id: _this.editId }
                })
                .then(function(res) {
                  console.log(res);
                  _this.tableData[_this.editIndex] = res.data["list"][0];
                });
            }
          }
          _this.reload();
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
            that.sendPostRequest("/api/teacher/mod", opt);
          } else {
            // 新增
            that.sendPostRequest("/api/teacher/add", that.simplify(that.form));
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
            _this.$message.error("查询教师失败");
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
      this.form.title = selfData.title;
      this.form.person_id_type = selfData.person_id_type;
      this.form.person_id = selfData.person_id;
      this.form.country = selfData.country;
      this.form.birth = selfData.birth;
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
      this.sendGetRequest("/api/teacher/del", {
        params: { id: this.delId }
      });
    },

    // mysearchData() {
    //   console.log(this.simplify(this.form));
    //   this.sendGetRequest("/api/teacher/get", {
    //     params: this.simplify(this.form)
    //   });
    // },

    mysearchData() {
      var _this = this;
      let newform = [_this.form];
      let j = 1;
      for (let key in _this.form) {
        if (_this.form[key] instanceof Array) {
          if (_this.form[key].length > 1) {
            j = newform.length;
            for (let i = 0; i < j; i++) {
              //实现深拷贝
              let _obj = JSON.stringify(newform[i]);
              let subform = JSON.parse(_obj);
              newform.push(subform);
            }
          }

          for (let i = 0; i < _this.form[key].length; i++) {
            newform[j + i - 1][key.substr(0, key.length - 1)] =
              _this.form[key][i];
          }
        }
      }
      _this.tableData = [];
      for (let i = 0; i < newform.length; i++) {
        _this.$http
          .get("/api/teacher/get", { params: _this.simplify(newform[i]) })
          .then(function(res) {
            //if (res.data["list"].length !== 0)
            let k = _this.tableData.length;
            if (res.data["list"].length !== 0)
              _this.tableData.push.apply(_this.tableData, res.data["list"]);
          });
      }
      this.reload();
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
    },
    handleCommand(command) {
      switch (command) {
        case "a":
          this.showid = !this.showid;
          console.log(this.showid);
      }
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

