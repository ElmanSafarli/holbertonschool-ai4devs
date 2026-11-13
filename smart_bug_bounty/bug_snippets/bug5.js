"use strict";

// Exercise: fetch all user records and keep the requested ID order.
async function loadUsers(ids, fetchUser) {
  const users = [];
  ids.forEach(async (id) => {
    const user = await fetchUser(id);
    users.push(user);
  });
  return users;
}

async function demo() {
  const fakeFetch = async (id) => ({ id, name: "User " + id });
  const users = await loadUsers([1, 2], fakeFetch);
  console.log(JSON.stringify(users));
}
if (require.main === module) {
  demo().catch(console.error);
}
module.exports = { loadUsers };
