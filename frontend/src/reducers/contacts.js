export const contacts = (state = [], action) => { // (1)
  switch (action.type) { // (2)
    case 'FETCH_CONTACTS_SUCCESS':
      return [
        ...action.contacts
      ]
    default:
      return state
  }
}
