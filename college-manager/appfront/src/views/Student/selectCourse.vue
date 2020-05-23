<template>
	<div>
        <div style="display: inline-block;float: right;">
            <el-button type="warning" plain @click="dialogFormSearch = true">搜索</el-button>
        </div>
		<div>
			<el-table
            :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
          :row-class-name="tableRowClassName"
	      stripe
	      style="width: 100%">
	      <el-table-column
	        prop="course_id"
            sortable
	        label="课程号">
	      </el-table-column>
	      <el-table-column
	        prop="course_name"
            sortable
	        label="课程名">
	      </el-table-column>
          <el-table-column
	        prop="teacher_name"
            sortable
	        label="开课教师">
	      </el-table-column>
          <el-table-column
	        prop="year"
            sortable
	        label="开课学年">
	      </el-table-column>
          <el-table-column
	        prop="term"
            sortable
	        label="开课学期">
	      </el-table-column>
          <el-table-column
	        prop="time"
            sortable
	        label="上课时间">
	      </el-table-column>
	      <el-table-column
	        prop="assessment"
            sortable
	        label="考核方式">
	      </el-table-column>
	      <el-table-column
	        prop="major_name"
            sortable
	        label="开课专业">
	      </el-table-column>
          <el-table-column
            fixed="right">
            <template slot="header">
                <el-input
                    prefix-icon="el-icon-search"
                    v-model="search"
                    size="mini"
                />
            </template>
            <template slot-scope="scope">
                <el-button v-if="!scope.row.is_selected" @click="addSelection(scope.$index)" type="text" size="small">选中</el-button>
                <el-button v-if="scope.row.is_selected" @click="delSelection(scope.$index)" type="text" size="small">退课</el-button>
            </template>
	      </el-table-column>
	    </el-table>
          <el-dialog title="请填写搜索信息(可只填部分)" :visible.sync="dialogFormSearch" style="height: 100%；">
        <el-form :model="form" :rules="rules" ref="form">
          <el-form-item label="课程号" prop="course_id">
            <el-input v-model="form.course_id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="授课老师工号" prop="teacher_id">
            <el-input v-model="form.teacher_id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课学年" prop="year">
            <el-input v-model="form.year" autocomplete="off" placeholder="年"></el-input>
          </el-form-item>
          <el-form-item label="开课学期" prop="term">
            <el-select style='width: 100%; position: absolute; left: 138px' v-model="form.term" placeholder="请选择学期">
              <el-option style='height: 80%' label="春" value="春" autocomplete="off"></el-option>
              <el-option style='height: 80%' label="秋" value="秋" autocomplete="off"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="开课时间" prop="time">
            <el-input v-model="form.time" autocomplete="off" placeholder="周一至周五的第一到第九节(周一第5节记作15)"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormSearch = false">取 消</el-button>
          <el-button type="primary" @click="submitSearch">确 定</el-button>
        </div>
      </el-dialog>

	  </div>
	</div>
</template>
<style lang='scss'>
	 @import "../../static/css/base.scss";
	.font {
		@include fontTwo()
	}
	.text {
		@include fontThree()
	}
    .el-table .selected-row{
        background: #f0f8eb;
    }
</style>
<script>
export default {
	name: "index",
	data() {
    return {
    	tableData: [],
      rules: {
      },
      form: {

      },
      search: '',
      dialogFormSearch: false,
    }
  },
  methods: {
		getAllData() {
            var _this = this
            var ldata=[]
	      _this.$http.get('/api/lecture/get',{params:{student_id:localStorage['id']}}).then(function (res) {
	    //   console.log(res)
          ldata = res.data.list
          _this.addSelected(ldata)
	    })
	    .catch(function (error) {
	      console.log(error)
        })
        
      },
      transData(){
        var a={"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9}
        var b=["一","二","三","四","五","六","七","八","九"]
        var c=["春","秋"]
        var d={"春":0,"秋":1}
        console.log(this.tableData)
        for(var i = 0; i <this.tableData.length;i++){
          if(isNaN(this.tableData[i].time)){
            this.tableData[i].time = 10*a[this.tableData[i].time.charAt(2)]+a[this.tableData[i].time.charAt(4)]
          }else{
            this.tableData[i].time = "星期"+b[Math.floor(this.tableData[i].time/10)-1]+"第"+b[this.tableData[i].time%10-1]+"节课"
          }
          if(!isNaN(this.tableData[i].assessment)){
            this.tableData[i].assessment = (this.tableData[i].assessment==0)?"考试":"论文";
          }else{
            this.tableData[i].assessment = (this.tableData[i].assessment=="考试")?0:1;
          }
          if(!isNaN(this.tableData[i].term)){
            this.tableData[i].term = c[this.tableData[i].term]
            console.log(this.tableData[i])
          }else{
            this.tableData[i].term = d[this.tableData[i].term]
          }
        }
      },
      addSelected(ldata){
          var _this = this
          this.$http.get('/api/selection/get',{params:{student_id:localStorage['id']}}).then(function(res){
            if(res.data.list.length==0){
              _this.tableData=ldata
            _this.transData()
              return
            }
            var data = res.data.list
            for(var i=0;i<ldata.length;i++){
              ldata[i].is_selected=false
            }
            for(var i=0;i<data.length;i++){
                for(var j=0;j<ldata.length;j++){
                    if(data[i].lecture_id==ldata[j].id &&(ldata[j].is_selected ||!ldata[j].is_selected)){
                        ldata[j].is_selected = true
                        _this.tableData.unshift(ldata[j])
                    }
                }
            }
            for(var i=0;i<ldata.length;i++){
              if(!ldata[i].is_selected)
                _this.tableData.push(ldata[i])
            }
          _this.transData()
        })

      },
	  searchData() {
	    var _this = this
      console.log(_this.tableData)
      var result = _this.tableData.filter(function(value, index, arr) {
        // console.log(value)
        // console.log(document.getElementsByClassName('sc')[0].value)
        return document.getElementsByClassName('sc')[0].value == value.courseName || document.getElementsByClassName('sc')[0].value == value.courseTime || document.getElementsByClassName('sc')[0].value == value.courseGrade
      })
      // console.log(result)
      _this.tableData = result
    },
    tableRowClassName({row,rowIndex}){
        if(this.tableData[rowIndex].is_selected){
            return 'selected-row'
        }else{
            return ''
        }
    },
    simplify(obj) {
      let newobj = new Object();
      for (let key in obj) {
        if (
          obj[key] &&
          key !== "id" &&
          key !== "course_id" &&
          key !== "teacher_id" &&
          key !== "term" &&
          key !== "time" &&
          key !== "year"
        )
          newobj[key] = obj[key];
      }
      return newobj;
    },
    addSelection(index){
        var _this = this
        var row = this.tableData[index]
        this.tableData[index].is_selected=true;
        var data={"lecture_id":row.id,"student_id":localStorage['id']}
        this.$http.post("/api/selection/add",data).then(function(res){
        }).catch(function (error) {
	      console.log(error)
        })
    },
    delSelection(index){
        var _this = this
        var row = _this.tableData[index]
        _this.tableData[index].is_selected=false
        var data={"lecture_id":row.id,"student_id":localStorage['id']}
        this.$http.get("/api/selection/del",{params:data}).then(function (res){
        }).catch(function (error) {
            console.log(error)
        })
    },
    submitSearch(){
        var _this = this
        if(this.form.term=="春")this.form.term=0
        else if(this.form.term=="秋")this.form.term=1
        else{}
        var newform={}
        for(let key in this.form){
          if(this.form[key]||this.form[key]==0){
            newform[key]=this.form[key]
          }
        }
        var ldata;
        this.$http.get("/api/lecture/get",{params:newform}).then(function (res){
          ldata=res.data.list
          this.tableData=[]
          _this.addSelected(ldata)
          _this.dialogFormSearch = false
        }).catch(function (error) {
            console.log(error)
        })
    }

  },

  mounted: function() {
    // 组件创建时候去获取所有的用户数据
    this.getAllData();
  }
}
</script>