-- ============================================================
-- UPSC Prep App — Supabase schema for auth, profiles, scores, leaderboard
-- Run this once in: Supabase Dashboard -> SQL Editor -> New query -> paste -> Run
-- ============================================================

-- 1. PROFILES table (one row per signed-up user, holds their display name)
create table if not exists public.profiles (
  id uuid references auth.users(id) on delete cascade primary key,
  username text unique not null,
  created_at timestamptz default now()
);

alter table public.profiles enable row level security;

-- Anyone (including anonymous visitors) can read usernames -- needed to show names on the leaderboard
create policy "Profiles are viewable by everyone"
  on public.profiles for select
  using (true);

-- A user can only create their own profile row
create policy "Users can insert their own profile"
  on public.profiles for insert
  with check (auth.uid() = id);

-- A user can only update their own profile row
create policy "Users can update their own profile"
  on public.profiles for update
  using (auth.uid() = id);


-- 2. QUIZ_ATTEMPTS table (one row per completed test)
create table if not exists public.quiz_attempts (
  id bigint generated always as identity primary key,
  user_id uuid references auth.users(id) on delete cascade not null,
  subject text not null,          -- e.g. 'polity', 'economy'
  chapter_id text,                -- null for a "Full Subject Test"
  chapter_title text not null,    -- e.g. 'Fundamental Rights' or 'Full Polity Test'
  level text not null,            -- 'basic' | 'intermediate' | 'advanced'
  total_questions int not null,
  correct_count int not null,
  score_pct int not null,
  taken_at timestamptz default now()
);

alter table public.quiz_attempts enable row level security;

-- Anyone can read all attempts -- needed to compute the leaderboard across all users
create policy "Quiz attempts are viewable by everyone"
  on public.quiz_attempts for select
  using (true);

-- A user can only insert an attempt row as themselves
create policy "Users can insert their own attempts"
  on public.quiz_attempts for insert
  with check (auth.uid() = user_id);

-- Helpful index for looking up a user's own history quickly
create index if not exists quiz_attempts_user_id_idx on public.quiz_attempts(user_id);
