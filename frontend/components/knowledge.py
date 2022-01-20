import streamlit as st
import requests
import json
import io


def load(modality, query):
    thoughts = []
    query_embeddings = None

    for microverse in st.session_state.get('microverses', []):
        url = microverse['url']
        url += '/find'

        if modality == 'text':
            response = requests.get(url, params={
                'token': microverse['token'],
                'query': query
            })
        elif modality == 'image':
            response = requests.post(url, data={
                'token': microverse['token']}, files={
                'query': query
            })

        content = json.loads(response.content)
        new_thoughts = content['authorized_thoughts']
        for e_idx, e in enumerate(new_thoughts):
            new_thoughts[e_idx]['conceptarium_url'] = microverse['url']
            new_thoughts[e_idx]['access_token'] = microverse['token']
            new_thoughts[e_idx]['auth'] = microverse['auth']

        if isinstance(content, dict):
            thoughts += content['authorized_thoughts']
            query_embeddings = content['query_embeddings']

    return query_embeddings, thoughts
