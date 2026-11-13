"use strict";
const { test } = require("node:test");
const assert = require("node:assert/strict");
const { cartTotal } = require("../bug2_fixed.js");
const { loadUsers } = require("../bug5_fixed.js");

test("bug2: original cart includes final item", () => {
  assert.equal(cartTotal([{price: 10, quantity: 2}, {price: 5, quantity: 3}]), 35);
});
test("bug2: empty cart", () => assert.equal(cartTotal([]), 0));
test("bug2: single item", () => assert.equal(cartTotal([{price: 5, quantity: 3}]), 15));
test("bug2: zero quantities and prices", () => {
  assert.equal(cartTotal([{price: 8, quantity: 0}, {price: 0, quantity: 9}]), 0);
});

test("bug5: stays pending until every fetch finishes and preserves order", async () => {
  const pending = new Map();
  let settled = false;
  const resultPromise = loadUsers([1, 2], id => new Promise(resolve => pending.set(id, resolve)));
  resultPromise.then(() => { settled = true; });
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(settled, false);
  pending.get(2)({id: 2});
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(settled, false);
  pending.get(1)({id: 1});
  const result = await resultPromise;
  assert.deepEqual(result, [{id: 1}, {id: 2}]);
  await new Promise(resolve => setImmediate(resolve));
  assert.deepEqual(result, [{id: 1}, {id: 2}]);
});
test("bug5: empty IDs do not invoke fetch", async () => {
  assert.deepEqual(await loadUsers([], () => { throw new Error("must not run"); }), []);
});
test("bug5: rejected fetch propagates the same error", async () => {
  const error = new Error("fetch failed");
  await assert.rejects(loadUsers([1], async () => { throw error; }), e => e === error);
});
test("bug5: synchronous throw becomes rejection", async () => {
  const error = new Error("sync failure");
  await assert.rejects(loadUsers([1], () => { throw error; }), e => e === error);
});
test("bug5: immediate values and duplicate IDs keep order", async () => {
  assert.deepEqual(await loadUsers([2, 1, 2], id => ({id})), [{id: 2}, {id: 1}, {id: 2}]);
});
test("bug5: repeated calls have independent results", async () => {
  const first = await loadUsers([1], async id => ({id}));
  const second = await loadUsers([2], async id => ({id}));
  assert.notStrictEqual(first, second);
  assert.deepEqual(first, [{id: 1}]);
  assert.deepEqual(second, [{id: 2}]);
});
