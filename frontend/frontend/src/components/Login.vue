<template>
    <div>
        <div class="header cov">
            <div class="logo"><img src="../assets/brickslogo.png" alt=""></div>
            <div><a href="./Homepage">回首頁</a></div>
        </div>
        <div class="middle cov">
            <div class="title">登入</div>
            <div class="enter">
                <input type="text" placeholder="帳號" id="account" v-model="account" ref="account">
                <div class="wrong accountx" ref="wrong1">{{ accountError }}</div>
                <input v-if="showPassword" type="text" v-model="password" placeholder="密碼" ref="password" id="password">
                <input v-else type="password" v-model="password" placeholder="密碼" ref="password" id="password">
                <button id="eye" @click="eyebtn"><img src="../assets/eye.png" alt=""></button>
            </div>
            <div class="wrong passwordx" ref="wrong2">{{ passwordError }}</div>
            <div class="keep_login">
                <div id="che">
                    <input type="checkbox" id="check1">
                    <label for="check1">保持登入</label>
                </div>
                <a href="https://www.youtube.com/">忘記密碼</a>
            </div>
            <!-- 目前先設定按登入後不論輸入什麼都會跑出錯誤的樣式 -->
            <button class="login" @click="Login">登入</button>
            <div>{{ loginTest }}</div>
            <div class="register">
                <p>還沒有帳戶？</p>
                <a href="./Register">註冊</a>
            </div>
            <div class="line">
                <div class="leftline"></div>
                <p>或</p>
                <div class="rightline"></div>
            </div>
            <div class="from_other">
                <a href="https://www.google.com.tw/?hl=zh_TW" class="google">
                    <img src="../assets/google.png" alt="">
                    <p>Google登入</p>
                </a>
                <a href="https://www.facebook.com/" class="facebook">
                    <img src="../assets/facebook.png" alt="">
                    <p>Facebook登入</p>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'Login',
    data() {
        return {
            showPassword: false,
            account: "",
            password: "",
            accountError: "1",
            passwordError: "2",
            loginTest: "現在還沒有按登入鍵",
        };
    },
    methods: {
        eyebtn() {
            this.showPassword = !this.showPassword;
        },
        Login() {
            //前端部分先進行帳號密碼原則檢驗，還有其他條件式
            if (this.password == "" || this.account == "") {
                this.$refs.account.style = "border-color : #e03939";
                this.$refs.password.style = "border-color : #e03939";
                this.$refs.wrong1.style = "display : block";
                this.$refs.wrong2.style = "display : block";
                this.accountError = "帳號錯誤或不存在";
                this.passwordError = "帳號錯誤或不存在";
                this.loginTest = "前端block";
            } else {
                const path = "http://localhost:5000/login";
                const user = { account: this.account, password: this.password };
                this.account = "";
                this.password = "";
                axios
                    .post(path, user)
                    .then((res) => {
                        if (res.data.status = 'success') {
                            this.goToPersonalPage();
                            this.loginTest = res.data.message;
                        } else {
                            this.$refs.account.style = "border-color : #e03939";
                            this.$refs.password.style = "border-color : #e03939";
                            this.$refs.wrong1.style = "display : block";
                            this.$refs.wrong2.style = "display : block";
                            this.accountError = res.data.accountError;
                            this.passwordError = res.data.passwordError;
                            this.loginTest = res.data.message;
                        }

                    })
                    .catch((error) => {
                        console.log(error);

                    });
            }

        },
        goToPersonalPage() {
            console.log("goToPersonalPage");
        }
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
    width: 34.375vw;
    height: 670px;
    position: relative;
}

.title {
    width: auto;
    height: 10%;
    font-size: 3vw;
    position: absolute;
    left: 50%;
    top: 0px;
    transform: translate(-50%);
    font-weight: 400;
}

.enter {
    width: 80.3%;
    height: 23.88%;
    position: absolute;
    top: 21.64%;
    left: 9.85%;
}

.enter input {
    width: 100%;
    height: 36.25%;
    border: 1px solid #9c9c9c;
    border-radius: 10px;
    font-size: 1vw;
    text-indent: 1em;
}

.wrong {
    font-size: 1vw;
    color: #e03939;
    position: absolute;
    display: none;
}

.accountx {
    top: 39.375%;
    left: 3.783%;
}

.passwordx {
    top: 45.97%;
    left: 12.8788%;
}

#password {
    position: absolute;
    bottom: 0;
}

.enter button {
    position: absolute;
    width: 1.8vw;
    height: 20%;
    top: 71%;
    left: 90%;
    border: none;
    cursor: pointer;
    background-color: transparent;
}

.enter img {
    width: 100%;
    height: 100%;
}

.keep_login {
    width: 74.24%;
    height: 2vw;
    position: absolute;
    top: 50.746%;
    left: 12.88%;
}

.keep_login label {
    font-size: 1.1vw;
    color: #676767;
    position: absolute;
    left: 5.045%;
    line-height: 100%;
}

.keep_login input {
    height: 1.1vw;
    width: 4%;
    position: absolute;
}

.keep_login a {
    font-size: 1.1vw;
    color: #676767;
    float: right;
    text-decoration: none;
    vertical-align: middle;
    line-height: 100%;
}

.login {
    width: 80%;
    height: 7.164%;
    border: 1px solid #9A2B2E;
    border-radius: 50px;
    background-color: #9A2B2E;
    cursor: pointer;
    font-size: 1.3vw;
    color: white;
    position: absolute;
    top: 60.447%;
    left: 9.8485%;
}

.register {
    width: auto;
    height: 3.582%;
    position: absolute;
    top: 70.895%;
    left: 50%;
    transform: translate(-50%);
    margin-bottom: 9.85%;
}

.register p {
    font-size: 1.1vw;
    float: left;
    color: #676767;
}

.register a {
    font-size: 1.1vw;
    color: #1977f3;
    text-decoration: none;
    float: left;
}

.line .leftline {
    position: absolute;
    left: 0;
    top: 82.836%;
    border-bottom: 2px solid #bcbcbc;
    width: 47.73%;
    height: 12px;
}

.line p {
    position: absolute;
    left: 48.485%;
    font-size: 1.1vw;
    color: #676767;
    top: 82.985%;

}

.line .rightline {
    position: absolute;
    left: 52.773%;
    top: 82.836%;
    border-bottom: 2px solid #bcbcbc;
    width: 47.73%;
    height: 12px;
}

.from_other {
    width: 80.3%;
    height: 8.955%;
    position: absolute;
    top: 91.045%;
    left: 50%;
    transform: translate(-50%);
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
    height: 58.33%;
    width: 14%;
    position: absolute;
    top: 21.67%;
    left: 12%;
}

.from_other p {
    font-size: 100%;
    display: inline-block;
    position: absolute;
    top: 25%;
    left: 40%;
}

.google {
    float: left;
}

.facebook {
    float: right;
}

.facebook p {
    left: 36%;
}

.from_other a:active {
    color: #676767;
}
</style>