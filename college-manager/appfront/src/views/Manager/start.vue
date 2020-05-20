<template>
	<div>
		<div>
			<div style='height: 80px'>
		      <h2 class='font' style="text-align: center;">HELLO WORLD</h2>
		  </div>

		</div>
		 	<div class='left'>
		 		<p>我喜欢数据库</p>
		 		<p>我太喜欢数据库了</p>
		 		<p>我永远喜欢数据库</p>
		 		<!--img src="../../../public/img/start5.jpg" alt=""-->
		 	</div>
			<el-calendar v-model="value">
			</el-calendar>

	</div>
</template>
<style lang='scss'>
  @import "../../static/css/base.scss";
  .font {
    @include fontTwo()
  }
  .text {
    @include fontThree()
    float: left;
  }
  .left {
  	margin-top: 42px;
  	width: 45%;
  	float: left;
  	p {
  		height: 18px;
  		line-height: 18px;
  		text-indent: 2em;
      font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
      font-size:18x;
      color:#999999;

  	}
  	img {
	  	width: 103%;

	  	float: left;
	  	margin-right: 20px;
	  }
  }

  .el-calendar {
  	float: right;
  	width: 45%;
  	height: 80%;
  	margin-top: 36px;
    color: blue;
  }

</style>
<script>
  export default {
    data() {
      return {
        value: new Date(),
      //   imgList: [
	     //    {id:0, src:'../../../public/img/start3.jpg'},
	     //    {id:1, src:'../../../public/img/start4.jpg'},
	     //    {id:2, src:'../../../public/img/start.jpg'},
	     //    {id:3, src:'../../../public/img/start5.jpg'}
	     // ]
      }
    }
  }
</script>30