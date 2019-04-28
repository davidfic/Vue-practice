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
        commit('setChores', response.data);
    }
};

const mutations = {
    setChores:  (state, chores) => (state.chores = chores)
};

export default {
    state,
    getters,
    actions,
    mutations
};