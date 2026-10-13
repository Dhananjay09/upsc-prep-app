/* On-device replacement for @supabase/supabase-js. No server, no login: one local user, data kept in localStorage. */
(function(){
  var KEY = 'upsc_pwa_db_v1';
  var USER = { id: 'local-device-user', email: 'device@local', user_metadata: { username: 'Me' } };
  var mem = null;

  function load(){
    if(mem) return mem;
    try{ var raw = localStorage.getItem(KEY); if(raw) mem = JSON.parse(raw); }catch(e){}
    if(!mem) mem = { profiles: [], quiz_attempts: [], seq: 0 };
    return mem;
  }
  function save(){ try{ localStorage.setItem(KEY, JSON.stringify(mem)); }catch(e){ console.warn('Could not persist scores:', e); } }

  function cmp(a, b){ return a < b ? -1 : a > b ? 1 : 0; }
  function passes(row, f){
    var v = row[f.col], x = f.val;
    switch(f.op){
      case 'eq': return v === x;
      case 'neq': return v !== x;
      case 'gt': return v > x; case 'gte': return v >= x;
      case 'lt': return v < x; case 'lte': return v <= x;
      case 'is': return (x === null) ? (v === null || v === undefined) : v === x;
      case 'in': return x.indexOf(v) !== -1;
      case 'not': return !passes(row, { col: f.col, op: f.inner, val: f.val });
    }
    return true;
  }
  function project(row, cols){
    if(!cols || cols.trim() === '*') return JSON.parse(JSON.stringify(row));
    var out = {}; cols.split(',').forEach(function(c){ c = c.trim(); if(c) out[c] = row[c]; });
    return out;
  }

  function Query(table){ this.t = table; this.op = 'select'; this.cols = '*'; this.f = []; this.o = []; this.lim = null; this.sg = null; this.row = null; this.ret = false; }
  Query.prototype.select = function(c){ if(this.op === 'insert') this.ret = true; else this.cols = c || '*'; return this; };
  Query.prototype.insert = function(r){ this.op = 'insert'; this.row = r; return this; };
  ['eq','neq','gt','gte','lt','lte','is','in'].forEach(function(op){
    Query.prototype[op] = function(col, val){ this.f.push({ col: col, op: op, val: val }); return this; };
  });
  Query.prototype.not = function(col, inner, val){ this.f.push({ col: col, op: 'not', inner: inner, val: val }); return this; };
  Query.prototype.order = function(col, opts){ this.o.push({ col: col, asc: !(opts && opts.ascending === false) }); return this; };
  Query.prototype.limit = function(n){ this.lim = n; return this; };
  Query.prototype.maybeSingle = function(){ this.sg = 'maybe'; return this; };
  Query.prototype.single = function(){ this.sg = 'single'; return this; };

  Query.prototype.run = function(){
    var db = load(), tbl = db[this.t];
    if(!tbl) return { data: null, error: { message: 'relation "' + this.t + '" does not exist' } };
    var rows;
    if(this.op === 'insert'){
      var r = JSON.parse(JSON.stringify(this.row));
      if(this.t === 'profiles'){
        if(db.profiles.some(function(p){ return p.username === r.username; }))
          return { data: null, error: { message: 'duplicate key value violates unique constraint "profiles_username_key"' } };
        r.created_at = new Date().toISOString();
      } else {
        r.id = ++db.seq; r.taken_at = new Date().toISOString();
      }
      tbl.push(r); save();
      if(!this.ret) return { data: null, error: null };
      rows = [r];
    } else {
      rows = tbl.filter(function(row){ return this.f.every(function(f){ return passes(row, f); }); }, this);
      for(var i = this.o.length - 1; i >= 0; i--){
        (function(o){ rows = rows.slice().sort(function(a, b){ return (o.asc ? 1 : -1) * cmp(a[o.col], b[o.col]); }); })(this.o[i]);
      }
      if(this.lim != null) rows = rows.slice(0, this.lim);
    }
    var data = rows.map(function(r){ return project(r, this.cols); }, this);
    if(this.sg === 'maybe'){ if(data.length > 1) return { data: null, error: { message: 'multiple rows returned' } }; return { data: data[0] || null, error: null }; }
    if(this.sg === 'single'){ if(data.length !== 1) return { data: null, error: { message: 'JSON object requested, multiple (or no) rows returned' } }; return { data: data[0], error: null }; }
    return { data: data, error: null };
  };
  Query.prototype.then = function(res, rej){ var out; try{ out = this.run(); }catch(e){ return Promise.reject(e).then(res, rej); } return Promise.resolve(out).then(res, rej); };

  var auth = {
    getSession: function(){ return Promise.resolve({ data: { session: { access_token: 'local', user: USER } }, error: null }); },
    signUp: function(){ return Promise.resolve({ data: { user: USER, session: { access_token: 'local', user: USER } }, error: null }); },
    signInWithPassword: function(){ return Promise.resolve({ data: { user: USER, session: { access_token: 'local', user: USER } }, error: null }); },
    signOut: function(){ return Promise.resolve({ error: null }); },
    onAuthStateChange: function(){ return { data: { subscription: { unsubscribe: function(){} } } }; }
  };

  window.__deviceDb = { reset: function(){ mem = { profiles: [], quiz_attempts: [], seq: 0 }; save(); } };
  window.supabase = { createClient: function(){ return { auth: auth, from: function(t){ return new Query(t); } }; } };
})();
