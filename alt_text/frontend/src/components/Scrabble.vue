<template>
    <div >
        <div id="scrabble" class="scrabble"> 
            <h1> Scrabble </h1>
        </div>
        <div>
            <div>
                <span>Type sentence here:</span>
                <br/>
                <input v-model="i_sentence" name="i_sentence" type="i_sentence" placeholder="...">
            </div>
            <div>
                <button type="submit" @click="scrabble_sentence"> 
                Scrabble
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div>
                 <span>Scrabbled sentence is:</span>
                 <br/>
                 <span>{{ output }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

// need for post method
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
    name: 'Scrabble',

    data: () => ({
        output: '',
        n_sentence: '',
    }),

    methods: {
        // Method to send sentence to Python to get alternatives
        scrabble_sentence : function() {
            this.output = this.i_sentence
            this.i_sentence = ''

            axios({
                method: "POST",
                url: "http://127.0.0.1:8000/api/scrabble/",
                headers: {'X-CSRFTOKEN': '{{ csrf_token }}', 'Content-Type': 'application/json'},
                data: {"sentence": this.output},
                responseType: 'json'
            }).then( function (response){
                console.log('Data returned = ' + response.data)
                this.n_sentence = response.data
            }).bind(this)
            .catch( function (error){
                console.log('Axios ajax error ' + error);
            })

        }
    },
}
</script>

<style scoped>
.scrabble h1 {
    color: green;
    font-size: 80px;
    margin: 40px;
}
span {
    margin: 0px;
}
button {
    background-color: green;
    margin: 20px;
    padding: 8px;
    border-radius: 8px;
    color: beige;
}
</style>
