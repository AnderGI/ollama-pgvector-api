CREATE SCHEMA backoffice;

CREATE TABLE backoffice.knowledge (
  id UUID PRIMARY KEY NOT NULL,
  category VARCHAR(255) NOT NULL,
  embedding VECTOR(768) NOT NULL
);
