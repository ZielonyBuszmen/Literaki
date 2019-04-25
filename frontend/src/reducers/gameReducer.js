//type": "BE_GAME_STATE", "password": "________ _____ _ ____", "category": "biedota"}

export const gameReducer = (state = [], action) => {
    console.log('asaasasdsa',action)
    switch (action.type) {
        case 'BE_GAME_STATE':
          return {...state, catchword: action.catchword }
        default:
            return state;
    }
}