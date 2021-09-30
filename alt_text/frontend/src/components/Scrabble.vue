<template>
    <div >
        <div class="scrabble"> 
            <h1> Scrabble </h1>
        </div>
        <div>
            <div>
                <p> Type sentence here: </p>
                <input v-model="sentence" placeholder="Type here">
            </div>
            <div>
                <button type="submit" > 
                Scrabble
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div>
                 <p>Input is: {{ sentence }}</p>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Scrabble',


}
</script>

<style scoped>
.scrabble h1 {
    color: green;
}
p {
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
