<template>
  <div>
    <div class="header cov">
      <div class="logo"><img src="../assets/brickslogo.png" alt="" /></div>
      <div><a href="./Homepage">回首頁</a></div>
    </div>
    <div class="middle cov">
      <p class="title">註冊</p>
      <div class="enter">
        <div class="account box">
          <p>帳號</p>
          <input type="text" placeholder="請輸入(規則)帳號名稱(不可改)" />
        </div>
        <div class="password box">
          <p>密碼</p>
          <input v-if="showPassword" type="text" placeholder="請輸入(規則)密碼" v-model="password" id="password"
            ref="password" />
          <input v-else type="password" placeholder="請輸入(規則)密碼" v-model="password" id="password" ref="password" />
          <button id="eye1" @click="eyebtn1"><img src="../assets/eye.png" alt="" /></button>
        </div>
        <div class="repassword box">
          <p>確認密碼</p>
          <input v-if="showRepassword" type="text" placeholder="請再次輸入您的密碼" v-model="repassword" id="repassword"
            ref="repassword" />
          <input v-else type="password" placeholder="請再次輸入您的密碼" v-model="repassword" id="repassword" ref="repassword" />

          <button id="eye2" @click="eyebtn2"><img src="../assets/eye.png" alt="" /></button>
        </div>
        <div class="email box">
          <p>電子信箱</p>
          <input type="email" placeholder="請填寫聯絡用電子信箱(可更改)" />
        </div>
      </div>
      <button class="login">註冊</button>
      <div class="already">
        <p>已經有帳戶？</p>
        <a href="./Login">登入</a>
      </div>
      <div class="line">
        <div class="leftline"></div>
        <p>或</p>
        <div class="rightline"></div>
      </div>
      <div class="from_other">
        <a href="https://www.google.com.tw/?hl=zh_TW" class="google">
          <img src="../assets/google.png" alt="" />
          <p>Google登入</p>
        </a>
        <a href="https://www.facebook.com/" class="facebook">
          <img src="../assets/facebook.png" alt="" />
          <p>Facebook登入</p>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      showPassword: false,
      password: null,
      showRepassword: false,
      repassword: null,
    };
  },
  methods: {
    eyebtn1() {
      this.showPassword = !this.showPassword;
    },
    eyebtn2() {
      this.showRepassword = !this.showRepassword;
    },
  },
  created() {

  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  font-family: "Noto Sans TC", sans-serif;
}

.cov {
  margin: 0 auto;
}

.header {
  position: relative;
  height: 111px;
  overflow: hidden;
  margin-bottom: 17px;
}

.header .logo {
  position: absolute;
  left: 3.229%;
}

.header img {
  height: 100%;
  width: auto;
}

.header a {
  position: absolute;
  top: 27%;
  right: 1.5625%;
  width: auto;
  border: 1px solid #676767;
  line-height: 47px;
  border-radius: 50px;
  text-align: center;
  font-size: 1vw;
  background-color: white;
  font-weight: 700;
  cursor: pointer;
  text-decoration: none;
  color: #363b3e;
  padding: 0 1.16% 0 1.16%;
}

.header a:active {
  color: #363b3e;
}

.middle {
  position: relative;
  width: 36.458vw;
  height: 774px;
}

.title {
  width: auto;
  height: 8.656%;
  line-height: 67px;
  font-size: 3vw;
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  top: 0;
}

.enter {
  height: 46.51%;
  width: 100%;
  position: absolute;
  top: 115px;
  left: 0;
}

.box {
  width: 90.714%;
  height: 16.66%;
  margin-bottom: 40px;
}

.enter .email {
  margin-bottom: 0;
}

.enter p {
  position: absolute;
  font-size: 1vw;
  color: #363b3e;
  font-weight: 700;
  display: inline-block;
}

.enter .account p {
  top: 5%;
  left: 5%;
}

.enter .password p {
  top: 33%;
  left: 5%;
}

.enter .repassword p {
  top: 61%;
}

.enter .email p {
  top: 88.5%;
}

.enter input {
  position: relative;
  left: 16.535%;
  width: 83.4646%;
  height: 100%;
  border: 1px solid #bfbfbf;
  border-radius: 10px;
  font-size: 1.1vw;
  padding-left: 1.1vw;
  display: inline-block;
}

.enter button {
  position: relative;
  top: 40%;
  transform: translate(0, -50%);
  left: 8.714%;
  border: none;
  background-color: white;
  cursor: pointer;
  background-color: transparent;
}

.login {
  width: 75.714%;
  height: 6.2%;
  border: 1px solid #9a2b2e;
  border-radius: 50px;
  background-color: #9a2b2e;
  cursor: pointer;
  font-size: 1.3vw;
  color: white;
  position: absolute;
  top: 67.183%;
  left: 15%;
  /* transform: translate(-50%); */
}

.already {
  width: auto;
  height: 3.1%;
  position: absolute;
  top: 76.227%;
  left: 50%;
  transform: translate(-50%);
}

.already p {
  font-size: 1.2vw;
  color: #676767;
  float: left;
}

.already a {
  font-size: 1.2vw;
  color: #1977f3;
  text-decoration: none;
}

.line .leftline {
  position: absolute;
  left: 5.714%;
  top: 86.82%;
  border-bottom: 2px solid #bcbcbc;
  width: 45%;
  height: 1px;
}

.line p {
  position: absolute;
  top: 85.57%;
  left: 51.4286%;
  font-size: 1.2vw;
  color: #676767;
}

.line .rightline {
  position: absolute;
  top: 86.82%;
  left: 55.3%;
  border-bottom: 2px solid #bcbcbc;
  width: 45%;
  height: 1px;
}

.from_other {
  width: 75.714%;
  height: 7.75%;
  position: absolute;
  top: 92.248%;
  left: 15%;
}

.from_other a {
  width: 47.17%;
  height: 100%;
  border: 1px solid #bfbfbf;
  border-radius: 10px;
  font-size: 100%;
  text-decoration: none;
  color: #676767;
  overflow: hidden;
  position: relative;
}

.from_other img {
  height: 58%;
  width: 14%;
  position: absolute;
  top: 21%;
  left: 10%;
}

.from_other p {
  font-size: 100%;
  display: inline-block;
  position: absolute;
  top: 50%;
  transform: translate(0, -50%);
  left: 45%;
}

.google {
  float: left;
}

.facebook {
  float: right;
}

.facebook p {
  left: 38%;
}

.from_other a:active {
  color: #676767;
}
</style>