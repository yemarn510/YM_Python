--
-- Name: book; Type: TABLE; Schema: public;
--

CREATE TABLE book (
    id integer NOT NULL,
    title character varying(64) NOT NULL,
    author character varying(20),
    publisher character varying(20),
    rentalStatus integer,
    summary character varying(200),
    releaseDate date,
    category character varying(20) NOT NULL
);

