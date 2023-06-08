"""Generative question-answering demo"""
import logging
import os
from pathlib import Path
import json

import hydra
from omegaconf import DictConfig

from mp_blog.llm_utils import (
    make_prompt, get_object_from_module, llm_generate,
    enforce_data_contract, EXPECTED_SCHEMA, DataContractError
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@hydra.main(version_base=None, config_path='.', config_name='config')
def main(cfg: DictConfig):
    logger.info('Creating prompt')
    prompt_str = cfg.template.format(
        context=cfg.context, question=cfg.question, answer_format=cfg.answer_format
    )
    logger.debug(f'Prompt text is {prompt_str}')

    prompt_dict = make_prompt(
        prompt_str=prompt_str,
        parent_module=cfg.generate_parent_module,
        object_name=cfg.generate_object
    )

    llm_generate_method = getattr(
        get_object_from_module(cfg.generate_parent_module, cfg.generate_object),
        cfg.generate_method
    )

    response_parser = get_object_from_module(
        cfg.response_parser_parent_module,
        cfg.response_parser_method
    )

    logger.info('Calling model')
    res = llm_generate(
        model_version=cfg.model_version, method=llm_generate_method,
        model_params=cfg.model_params,
        text_input_dict=prompt_dict, parser=response_parser
    )

    try:
        enforce_data_contract(res, EXPECTED_SCHEMA)
        data_contract_success = True
        logger.info("Response satisfies data contract")
    except DataContractError as _:
        data_contract_success = False
        logger.info("Response fails data contract")
    results_path = Path(os.getcwd()) / 'result.json'

    res_dict = dict(
        data_contract_success=data_contract_success,
        response=json.loads(res) if data_contract_success else res
    )

    logger.info(f'Writing results to {results_path}')
    with open(results_path, 'w') as fp:
        json.dump(res_dict, fp, indent=2)


if __name__ == '__main__':
    main()
