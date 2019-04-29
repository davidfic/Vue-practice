import axios from 'axios';

const state = {
    chores: []
};

const getters = {
    allChores: (state) => state.chores
};

const actions  = {
    async fetchChores({commit}) {
        const response = await axios.get('https://jsonplaceholder.typicode.com/todos');
        // const response = await axios.get('http://localhost:5000/chores');
        commit('setChores', response.data);
    },
    async addChore({commit}, title) {
        const response = await axios.post('https://jsonplaceholder.typicode.com/todos', {title, completed: false});
        commit('newChore', response.data);
    }
};

const mutations = {
    setChores:  (state, chores) => (state.chores = chores),
    newChore: (state, chore) => state.chores.unshift(chore)
};

export default {
    state,
    getters,
    actions,
    mutations
};